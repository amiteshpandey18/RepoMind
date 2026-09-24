from src.repomind.rag.rag_service import ask_repository


answer = ask_repository(
    owner="amiteshpandey18",
    repo="RepoMind",
    question="What does this project use for authentication?"
)


print()
print("==============================")
print("RAG Answer")
print("==============================")
print(answer)