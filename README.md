# 🚀 GenAI Healthcare Backend

*Your intelligent healthcare assistant powered by FastAPI, Neo4j Desktop, and Hugging Face models.*

---

## 🔍 Project Overview

𝐓𝐡𝐢𝐬 𝐛𝐚𝐜𝐤𝐞𝐧𝐝 𝐩𝐨𝐰𝐞𝐫𝐬 𝐭𝐡𝐞 **𝐆𝐞𝐧𝐀𝐈 𝐇𝐞𝐚𝐥𝐭𝐡𝐜𝐚𝐫𝐞 𝐂𝐡𝐚𝐭𝐛𝐨𝐭**, 𝐚 𝐬𝐦𝐚𝐫𝐭 𝐚𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐭𝐡𝐚𝐭 𝐥𝐞𝐯𝐞𝐫𝐚𝐠𝐞𝐬 𝐚 𝐥𝐨𝐜𝐚𝐥 𝐠𝐫𝐚𝐩𝐡 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐚𝐧𝐝 𝐬𝐭𝐚𝐭𝐞-𝐨𝐟-𝐭𝐡𝐞-𝐚𝐫𝐭 𝐍𝐋𝐏 𝐦𝐨𝐝𝐞𝐥𝐬 𝐭𝐨 𝐚𝐧𝐬𝐰𝐞𝐫 𝐡𝐞𝐚𝐥𝐭𝐡𝐜𝐚𝐫𝐞-𝐫𝐞𝐥𝐚𝐭𝐞𝐝 𝐪𝐮𝐞𝐫𝐢𝐞𝐬 𝐰𝐢𝐭𝐡 𝐜𝐨𝐧𝐭𝐞𝐱𝐭-𝐚𝐰𝐚𝐫𝐞 𝐩𝐫𝐞𝐜𝐢𝐬𝐢𝐨𝐧.

- **𝐁𝐮𝐢𝐥𝐭 𝐰𝐢𝐭𝐡:** 𝐅𝐚𝐬𝐭𝐀𝐏𝐈, 𝐍𝐞𝐨𝟒𝐣 𝐃𝐞𝐬𝐤𝐭𝐨𝐩 (𝐥𝐨𝐜𝐚𝐥), 𝐇𝐮𝐠𝐠𝐢𝐧𝐠 𝐅𝐚𝐜𝐞 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐞𝐫𝐬  
- **𝐏𝐮𝐫𝐩𝐨𝐬𝐞:** 𝐃𝐞𝐥𝐢𝐯𝐞𝐫 𝐢𝐧𝐬𝐢𝐠𝐡𝐭𝐟𝐮𝐥, 𝐩𝐚𝐭𝐢𝐞𝐧𝐭-𝐜𝐞𝐧𝐭𝐫𝐢𝐜 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞𝐬 𝐛𝐲 𝐪𝐮𝐞𝐫𝐲𝐢𝐧𝐠 𝐠𝐫𝐚𝐩𝐡 𝐝𝐚𝐭𝐚 𝐚𝐧𝐝 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐧𝐚𝐭𝐮𝐫𝐚𝐥 𝐥𝐚𝐧𝐠𝐮𝐚𝐠𝐞 𝐚𝐧𝐬𝐰𝐞𝐫𝐬.
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

