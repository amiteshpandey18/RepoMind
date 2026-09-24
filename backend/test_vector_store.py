from src.repomind.rag.embeddings import create_embedding
from src.repomind.rag.vector_store import add_chunk


text = "FastAPI uses Pydantic for data validation."


embedding = create_embedding(text)


add_chunk(
    chunk_id="test-1",
    content=text,
    embedding=embedding,
    file_path="test.py"
)


print("Chunk stored successfully in ChromaDB")
