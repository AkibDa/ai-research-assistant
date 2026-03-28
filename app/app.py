from fastapi import FastAPI
from app.routes import chat, upload

app = FastAPI(title="AI Research Assistant")

app.include_router(chat.router, prefix="/chat")
app.include_router(upload.router, prefix="/upload")

@app.get("/")
def root():
    return {"message": "API is running"}
