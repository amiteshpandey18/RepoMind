from openai import OpenAI

from openai import OpenAI

from src.repomind.core.config import OPENAI_API_KEY


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def create_embedding(text: str):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


def create_embeddings(texts: list[str]):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )

    embeddings = []

    for item in response.data:
        embeddings.append(item.embedding)

    return embeddings
