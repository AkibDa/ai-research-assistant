# app/routes/chat.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import get_response
from app.services.auth_service import get_current_user
from fastapi import Depends

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/")
async def chat(req: ChatRequest, user: str = Depends(get_current_user)):
    response = get_response(req.query, user)
    return {"response": response}
