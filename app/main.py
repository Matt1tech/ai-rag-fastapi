from fastapi import FastAPI
from app.db.session import engine
from sqlalchemy import text

app = FastAPI(title="AI RAG System")


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            value = result.scalar()  # ✅ gets the single value (1)

            return {
                "status": "Database connected",
                "result": value
            }
    except Exception as e:
        return {"error": str(e)}