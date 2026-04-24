from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

from app.models import *  # ✅ MUST be before create_all

from app.api.auth import router as auth_router

app = FastAPI(title="AI RAG System")

# ✅ This runs AFTER models are loaded
Base.metadata.create_all(bind=engine)

app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "API is running"}