from openai import OpenAI

from repomind.core.config import OPENAI_API_KEY


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def create_embedding(text: str):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


def create_embeddings(
    texts: list[str],
    batch_size: int = 100
):

    all_embeddings = []

    for i in range(0, len(texts), batch_size):

        batch = texts[i:i + batch_size]

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=batch
        )

        for item in response.data:
            all_embeddings.append(
                item.embedding
            )

        print(
            f"Embedded {min(i + batch_size, len(texts))}/{len(texts)} chunks"
        )

    return all_embeddings
