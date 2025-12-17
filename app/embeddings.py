from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def embed_texts(texts: list[str]):
    return model.encode(texts).tolist()

def embed_query(query: str):
    return model.encode([query])[0].tolist()

