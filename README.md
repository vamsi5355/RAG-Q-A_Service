# RAG Q&A Service

A **production-ready Retrieval-Augmented Generation (RAG) backend service** built with **FastAPI**. This service allows users to ask questions and receive context-aware answers by combining vector search (embeddings) with LLM-based generation.

Designed to be **simple, scalable, and interview-ready**.

---

## ✨ Features

* 🔍 Semantic search using sentence embeddings
* 🧠 Context-aware question answering (RAG)
* ⚡ FastAPI-based REST API
* 🔄 Hot reload support for development
* 🧩 Modular and clean project structure
* 🐍 Python virtual environment friendly

---

## 🏗️ Project Structure

```
RAG-Q-A_Service/
│
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── embeddings.py   # Text & query embedding logic
│   ├── retriever.py    # Context retrieval logic
│   └── generator.py    # Answer generation logic
│
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore
└── venv/               # Virtual environment (ignored by git)
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/RAG-Q-A_Service.git
cd RAG-Q-A_Service
```

---

### 2️⃣ Create & activate virtual environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the FastAPI server

```bash
uvicorn app.main:app --reload --port 9000
```

Server will start at:
👉 **[http://127.0.0.1:9000](http://127.0.0.1:9000)**

API Docs:

* Swagger UI → `http://127.0.0.1:9000/docs`
* ReDoc → `http://127.0.0.1:9000/redoc`

---

## 🧠 How RAG Works (High Level)

1. User submits a question
2. Question is converted into an embedding vector
3. Relevant documents are retrieved using vector similarity
4. Retrieved context + user question is passed to the LLM
5. Final answer is generated and returned

This approach improves **accuracy**, **relevance**, and **hallucination control** compared to vanilla LLM prompts.

---

## 📦 Tech Stack

* **Backend:** FastAPI
* **Embeddings:** Sentence-Transformers
* **LLM Integration:** (Pluggable / configurable)
* **Language:** Python 3.11
* **Server:** Uvicorn

---

## 🛣️ Roadmap

* [ ] Add vector database (FAISS / Chroma)
* [ ] Add document ingestion pipeline
* [ ] Streaming responses
* [ ] Authentication & rate limiting
* [ ] Docker support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

Built with ❤️ by **Vamsi**

If you found this helpful, feel free to ⭐ the repository!
