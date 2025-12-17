import chromadb
from chromadb.config import Settings

client = chromadb.Client(
    Settings(persist_directory="data/chroma")
)

collection = client.get_or_create_collection(name="documents")

def add_chunks(chunks, embeddings):
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[f"chunk_{collection.count() + i}"]
        )

def query_chunks(query_embedding, k):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    return results["documents"][0]
