from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from repomind.agent.graph import app


router = APIRouter(prefix="/agent", tags=["Agent"])


class AgentRequest(BaseModel):
    question: str
    owner: str
    repo: str
    thread_id: str = "repo-1"


@router.post("/stream")
def stream_agent(request: AgentRequest):

    config = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    def generate():

        for chunk in app.stream(
            {
                "question": request.question,
                "owner": request.owner,
                "repo": request.repo,
                "context": "",
                "answer": "",
                "tool": "",
                "source": "",
                "messages": [
                    {
                        "role": "user",
                        "content": request.question
                    }
                ]
            },
            config=config,
            stream_mode="custom"
        ):
            yield chunk

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )
