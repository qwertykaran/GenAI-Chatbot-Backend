# 🚀 GenAI Healthcare Backend

*Your intelligent healthcare assistant powered by FastAPI, Neo4j Desktop, and Hugging Face models.*

---

## 🔍 Project Overview

𝑻𝒉𝒊𝒔 𝒃𝒂𝒄𝒌𝒆𝒏𝒅 𝒑𝒐𝒘𝒆𝒓𝒔 𝒕𝒉𝒆 **𝑮𝒆𝒏𝑨𝑰 𝑯𝒆𝒂𝒍𝒕𝒉𝒄𝒂𝒓𝒆 𝑪𝒉𝒂𝒕𝒃𝒐𝒕**, 𝒂 𝒔𝒎𝒂𝒓𝒕 𝒂𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝒕𝒉𝒂𝒕 𝒍𝒆𝒗𝒆𝒓𝒂𝒈𝒆𝒔 𝒂 𝒍𝒐𝒄𝒂𝒍 𝒈𝒓𝒂𝒑𝒉 𝒅𝒂𝒕𝒂𝒃𝒂𝒔𝒆 𝒂𝒏𝒅 𝒔𝒕𝒂𝒕𝒆-𝒐𝒇-𝒕𝒉𝒆-𝒂𝒓𝒕 𝑵𝑳𝑷 𝒎𝒐𝒅𝒆𝒍𝒔 𝒕𝒐 𝒂𝒏𝒔𝒘𝒆𝒓 𝒉𝒆𝒂𝒍𝒕𝒉𝒄𝒂𝒓𝒆-𝒓𝒆𝒍𝒂𝒕𝒆𝒅 𝒒𝒖𝒆𝒓𝒊𝒆𝒔 𝒘𝒊𝒕𝒉 𝒄𝒐𝒏𝒕𝒆𝒙𝒕-𝒂𝒘𝒂𝒓𝒆 𝒑𝒓𝒆𝒄𝒊𝒔𝒊𝒐𝒏.

- **𝑩𝒖𝒊𝒍𝒕 𝒘𝒊𝒕𝒉:** 𝑭𝒂𝒔𝒕𝑨𝑷𝑰, 𝑵𝒆𝒐4𝒋 𝑫𝒆𝒔𝒌𝒕𝒐𝒑 (𝒍𝒐𝒄𝒂𝒍), 𝑯𝒖𝒈𝒈𝒊𝒏𝒈 𝑭𝒂𝒄𝒆 𝑻𝒓𝒂𝒏𝒔𝒇𝒐𝒓𝒎𝒆𝒓𝒔  
- **𝑷𝒖𝒓𝒑𝒐𝒔𝒆:** 𝑫𝒆𝒍𝒊𝒗𝒆𝒓 𝒊𝒏𝒔𝒊𝒈𝒉𝒕𝒇𝒖𝒍, 𝒑𝒂𝒕𝒊𝒆𝒏𝒕-𝒄𝒆𝒏𝒕𝒓𝒊𝒄 𝒓𝒆𝒔𝒑𝒐𝒏𝒔𝒆𝒔 𝒃𝒚 𝒒𝒖𝒆𝒓𝒚𝒊𝒏𝒈 𝒈𝒓𝒂𝒑𝒉 𝒅𝒂𝒕𝒂 𝒂𝒏𝒅 𝒈𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒏𝒈 𝒏𝒂𝒕𝒖𝒓𝒂𝒍 𝒍𝒂𝒏𝒈𝒖𝒂𝒈𝒆 𝒂𝒏𝒔𝒘𝒆𝒓𝒔.
---
## 🛠 Tech Stack

**Frontend:**  
- React (JavaScript)
- Axios (API requests)
- HTML5 & CSS3 (inline styles, responsive design)

**Backend:**  
- FastAPI (Python)
- Uvicorn (ASGI server)
- Python-dotenv (env variable management)

**Database:**  
- Neo4j Desktop (Graph Database)

**AI/NLP:**  
- Hugging Face Transformers (flan-t5-large)

**Other Tools:**  
- Git & GitHub (version control)
- Visual Studio Code (recommended editor)
- REST Client (Postman or browser for API testing)

---
## 📜 Certification

This project was certified by **Intel®**.

[View Certificate (PDF)](INTEL_CERTIFICATE.pdf)

---
## ⚙️ Features

- FastAPI REST API with clean, scalable endpoints  
- Neo4j Desktop integration for complex healthcare graph queries  
- Hugging Face transformer model (e.g., `flan-t5-large`) for natural language understanding  
- `/chat` endpoint for interactive Q&A  
- Health check endpoint `/db-test` to verify Neo4j connectivity

---

## 🏗 Architecture

![Alt text](./ArchitectureDiagram.png)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+  
- Neo4j Desktop installed and running locally ([https://neo4j.com/docs/desktop-manual/current/installation/](https://neo4j.com/docs/desktop-manual/current/installation/))  
- Hugging Face API token (optional if using hosted inference)

## 🚀 Installation

```bash
git clone https://github.com/qwertykaran/genai-healthcare-backend.git
cd genai-healthcare-backend
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```


---

### Environment Variables

Create a `.env` file in the root directory:
```bash
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=<your-neo4j-password>
HF_MODEL_NAME=google/flan-t5-large
```

---

### Run the Backend

```bash

uvicorn main:app --reload
```

---

## 🧪 Testing the Backend

- **Health Check:**  
  Visit `http://localhost:8000`  

- **Chatbot Query:**  
Send a POST request to `/chat` with JSON body:  
{
"question": "What positive feedback have patients given about Dr. Joseph Johnson?"
}

---

## 📸 Screenshots

![Alt text](./Demo.png)

---

## ⚠️ Notes & Tips

- Make sure your Neo4j Desktop database is running before starting the backend.  
- Use the `bolt://localhost:7687` URI for local Neo4j connections.  
- Adjust Neo4j username and password in `.env` accordingly.

---

## 🔮 Future Enhancements

- Add authentication and user management  
- Deploy backend and frontend with CI/CD pipelines  
- Improve chatbot conversational abilities

---

## 📎 Links

- Frontend Repo: [genai-healthcare-frontend](https://github.com/qwertykaran/GenAI-Chatbot-Frontend.git)  
- Neo4j Desktop Docs: [https://neo4j.com/docs/desktop-manual/current/](https://neo4j.com/docs/desktop-manual/current/)

---

## 📄 License

MIT License © 2025 Karan Soni

