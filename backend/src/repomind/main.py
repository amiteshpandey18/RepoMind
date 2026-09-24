from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from repomind.api.routes import router
from repomind.db.database import Base, engine
from repomind.db.models.user import User
from repomind.auth.routes import router as auth_router


app = FastAPI(
    title="RepoMind",
    description="AI-powered GitHub Repository Intelligence Platform"
)


Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
app.include_router(auth_router)