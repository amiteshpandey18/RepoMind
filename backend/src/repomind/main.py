from fastapi import FastAPI

from repomind.api.routes import router
from repomind.db.database import Base, engine
from repomind.db.models.user import User

app = FastAPI(title='RepoMind',
              description="AI-powered GitHub Repository Intelligence Platform")

Base.metadata.create_all(bind=engine)

app.include_router(router)
