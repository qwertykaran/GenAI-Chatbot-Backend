from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from neo4j import GraphDatabase
from transformers import pipeline
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache
from sentence_transformers import SentenceTransformer, util
from fuzzywuzzy import process
import os
import re

# --- FastAPI Setup ---
app = FastAPI()
import os



# @app.get("/db-test")
# def db_test():
#     uri = os.getenv("NEO4J_URI")
#     user = os.getenv("NEO4J_USERNAME")
#     pwd = os.getenv("NEO4J_PASSWORD")
#     driver = GraphDatabase.driver(uri, auth=(user, pwd))
#     with driver.session() as session:
#         result = session.run("RETURN 1 AS test")
#         return {"db_test": result.single()["test"]}
    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is running successfully 🚀"}

# --- Load Env & Neo4j Setup ---
load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

@app.on_event("shutdown")
def shutdown():
    driver.close()

# --- Hugging Face Model (lazy load) ---
@lru_cache()
def get_qa_pipeline():
    model_name = os.getenv("HF_MODEL_NAME", "google/flan-t5-base")
    print(f"Loading Hugging Face model: {model_name}")
    return pipeline("text2text-generation", model=model_name)

# --- Sentence Transformer Model (lazy load) ---
@lru_cache()
def get_sentence_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

# --- Request Schema ---
class QueryRequest(BaseModel):
    question: str

# --- Physician Utilities ---
def get_all_physician_names():
    cypher = "MATCH (p:Physician) RETURN DISTINCT p.name AS name"
    with driver.session() as session:
        results = session.run(cypher)
        return [record["name"] for record in results]

def extract_physician_name(question, physician_names):
    matches = process.extractBests(
        question, physician_names, score_cutoff=70, limit=1
    )
    return matches[0][0] if matches else None

# --- Neo4j Review Fetch ---
def get_reviews_from_neo4j(physician_name=None):
    if physician_name:
        cypher = """
        MATCH (p:Patient)-[:WROTE]->(r:Review)-[:ABOUT]->(doc:Physician {name: $name})
        RETURN doc.name AS physician, r.text AS review
        """
        params = {"name": physician_name}
    else:
        cypher = """
        MATCH (p:Patient)-[:WROTE]->(r:Review)-[:ABOUT]->(doc:Physician)
        RETURN doc.name AS physician, r.text AS review
        LIMIT 20
        """
        params = {}

    with driver.session() as session:
        results = session.run(cypher, **params)
        return [{"physician": r["physician"], "review": r["review"]} for r in results]

# --- Semantic Filtering of Reviews ---
def filter_relevant_reviews(question, reviews, top_k=10):
    if not reviews:
        return []
    model = get_sentence_model()
    question_embed = model.encode(question)
    review_texts = [r['review'] for r in reviews]
    review_embeddings = model.encode(review_texts)
    scores = util.dot_score(question_embed, review_embeddings)[0]
    sorted_reviews = sorted(
        zip(reviews, scores.tolist()),
        key=lambda x: x[1],
        reverse=True
    )
    return [r for r, score in sorted_reviews[:top_k]]

# --- Intent Detection ---
def detect_intent(question):
    q = question.lower()
    if any(word in q for word in ['problem', 'complaint', 'issue', 'bad', 'negative', 'drawback']):
        return 'complaint'
    if any(word in q for word in ['best', 'good', 'excellent', 'positive', 'praise', 'like', 'strength']):
        return 'praise'
    if any(word in q for word in ['compare', 'vs', 'versus', 'difference']):
        return 'comparison'
    return 'general'

# --- Remove Redundant Sentences ---
def remove_redundant_sentences(text):
    seen = set()
    sentences = []
    for sentence in re.split(r'(?<=[.?!])\s+', text):
        normalized = sentence.strip().lower()
        if normalized and normalized not in seen:
            seen.add(normalized)
            sentences.append(sentence.strip())
    return ' '.join(sentences)

# --- Context Builder with Intent Awareness ---
def get_context_from_neo4j(question, intent=None):
    try:
        physician_names = get_all_physician_names()
        matched_physician = extract_physician_name(question, physician_names)
        if matched_physician:
            reviews = get_reviews_from_neo4j(matched_physician)
        else:
            reviews = get_reviews_from_neo4j()  # general reviews

        # For praise/complaint, pass all reviews for best context
        if intent in ["praise", "complaint"]:
            filtered_reviews = reviews
        else:
            filtered_reviews = filter_relevant_reviews(question, reviews, top_k=10)
        context = "\n".join([r["review"] for r in filtered_reviews])
        return context, matched_physician
    except Exception as e:
        print("❌ Error fetching context from Neo4j:", str(e))
        return "", None

# --- Chat Endpoint with Intent-based Prompt ---
@app.post("/chat")
def chat(request: QueryRequest):
    try:
        intent = detect_intent(request.question)
        context, physician_name = get_context_from_neo4j(request.question, intent)
        if not context:
            return {"answer": "No reviews available."}

        qa = get_qa_pipeline()

        # Build prompt based on intent and context
        if physician_name:
            if intent == "complaint":
                prompt = f"""You are an AI assistant. ONLY summarize the recurring problems, complaints, or negative feedback from the following patient reviews about Dr. {physician_name}.
Do NOT include any positive feedback, compliments, or neutral statements.
If there are no complaints or negative feedback, reply with: "No complaints reported."

Reviews:
{context}

Answer:
"""
            elif intent == "praise":
                prompt = f"""You are an AI assistant. ONLY summarize the positive feedback, compliments, or strengths mentioned in the following patient reviews about Dr. {physician_name}.
Do NOT include any complaints, negative comments, or neutral statements.
If there is no positive feedback, reply with: "No positive feedback reported."

Reviews:
{context}

Answer:
"""
            elif intent == "comparison":
                prompt = f"""You are an AI assistant. Based ONLY on the following patient reviews, compare Dr. {physician_name} to other physicians mentioned.
Highlight any unique strengths or weaknesses of Dr. {physician_name} as described by patients.
If there is not enough information for a comparison, reply with: "No comparison available."

Reviews:
{context}

Answer:
"""
            else:
                prompt = f"""You are an AI assistant. Summarize the main points from the following patient reviews about Dr. {physician_name}.
Include both positive and negative feedback, but do not repeat the same point more than once.
If there are no reviews, reply with: "No reviews available."

Reviews:
{context}

Answer:
"""
        else:
            prompt = f"""You are an AI assistant. Based ONLY on the following patient reviews, answer the user's question about the hospital or its facilities.
Be specific and do not make up information.
If there are no relevant reviews, reply with: "No reviews available."

Reviews:
{context}

User Question:
{request.question}

Answer:
"""

        response = qa(prompt, max_new_tokens=200)[0]['generated_text']
        cleaned_response = remove_redundant_sentences(response.strip())
        if not cleaned_response or cleaned_response.lower() in [
            "no complaints reported.",
            "no positive feedback reported.",
            "no comparison available.",
            "no reviews available.",
            "no relevant feedback available."
        ]:
            cleaned_response = "No relevant feedback available."
        return {"answer": cleaned_response}

    except Exception as e:
        print("❌ Backend error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
