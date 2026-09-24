from src.repomind.rag.splitter import split_text


text = """
RepoMind is an AI-powered GitHub repository intelligence platform.

Users can explore GitHub repositories.

Users can view files and folders.

Users can view repository commit history.

In the future, RepoMind will use RAG to answer questions about repository code.

The system will use ChromaDB for vector search.

The system will use OpenAI for generating answers.
"""


chunks = split_text(text)


print("Number of chunks:", len(chunks))


for index, chunk in enumerate(chunks):

    print()
    print("Chunk", index + 1)
    print("----------------")
    print(chunk)