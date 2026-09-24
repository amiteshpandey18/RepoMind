from fastapi import APIRouter
from pydantic import BaseModel

from repomind.rag.rag_service import ask_repository


router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


class QuestionRequest(BaseModel):
    owner: str
    repo: str
    question: str


@router.post("/ask")
def ask_question(request: QuestionRequest):

    answer = ask_repository(
        owner=request.owner,
        repo=request.repo,
        question=request.question
    )

    return {
        "owner": request.owner,
        "repo": request.repo,
        "question": request.question,
        "answer": answer
    }
