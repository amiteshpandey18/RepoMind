from fastapi import APIRouter
from sqlalchemy import text

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
