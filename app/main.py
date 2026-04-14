from fastapi import FastAPI

app = FastAPI(title="AI RAG System")

@app.get("/")
def root():
    return {"message": "API is running"}
