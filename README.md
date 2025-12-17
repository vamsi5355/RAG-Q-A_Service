# RAG-Q-A_Service
# RAG Document Question Answering API

Project Overview
This project is a FastAPI-based Retrieval-Augmented Generation (RAG) service that allows users to upload documents and ask questions about their content. The system retrieves relevant document chunks using semantic similarity and generates context-aware answers using a Large Language Model (LLM).

Prerequisites
- Python 3.9 or higher
- Git
- OpenAI API key

Setup Instructions

Clone the repository
git clone https://github.com/vamsi5355/RAG-service.git
cd RAG-service

Create and activate a virtual environment
python -m venv venv

Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Configure environment variables
Create a .env file in the project root directory and add:
OPENAI_API_KEY=your_openai_api_key_here

Running the Application Locally
uvicorn app.main:app --reload

Application URL
http://127.0.0.1:8000

Swagger API documentation
http://127.0.0.1:8000/docs

API Documentation

POST /upload
Uploads a document, extracts text, chunks it, generates embeddings, and stores them in the vector database.

Supported file formats
.txt
.md
.pdf

Example using curl
curl -X POST "http://127.0.0.1:8000/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@rag_test_document.txt"

Response
{
  "message": "Document uploaded and indexed successfully"
}

POST /query
Accepts a question and returns an answer generated using retrieved document context.

Request body
{
  "question": "What is Retrieval-Augmented Generation?"
}

Example using curl
curl -X POST "http://127.0.0.1:8000/query" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"question\": \"What is Retrieval-Augmented Generation?\" }"

Response
{
  "answer": "Retrieval-Augmented Generation is a technique that combines information retrieval with text generation to produce more accurate responses.",
  "sources": [
    "Relevant document chunk 1...",
    "Relevant document chunk 2..."
  ]
}

GET /report
Returns basic evaluation metrics.

Example using curl
curl -X GET "http://127.0.0.1:8000/report"

Response
{
  "context_precision": 0.9,
  "faithfulness": 0.85
}

Conclusion
This project demonstrates a complete Retrieval-Augmented Generation pipeline with document ingestion, semantic retrieval, and context-aware question answering exposed through a RESTful API.
