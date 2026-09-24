from fastapi import APIRouter
from sqlalchemy import text
from repomind.services.github_service import get_repository
from repomind.db.database import engine


router = APIRouter()


@router.get("/")
def root():
    return {"message": "Welcome to RepoMind"}


@router.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
        }


@router.get("/github/{owner}/{repo}")
def github_repository(owner: str, repo: str):
    repository = get_repository(owner, repo)

    if repository is None:
        return {
            "message": "Repository not found"
        }

    return {
        "name": repository["name"],
        "full_name": repository["full_name"],
        "description": repository["description"],
        "language": repository["language"],
        "stars": repository["stargazers_count"],
        "forks": repository["forks_count"],
        "url": repository["html_url"],
    }