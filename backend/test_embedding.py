from src.repomind.rag.embeddings import create_embedding


text = "FastAPI uses Pydantic for data validation."


embedding = create_embedding(text)


print("OpenAI is working")
print("Embedding dimensions:", len(embedding))
print("First 5 values:", embedding[:5])