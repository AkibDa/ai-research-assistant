from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import get_response

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/")
async def chat(req: ChatRequest):
    response = get_response(req.query)
    return {"response": response}