# app/routes/chat.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import get_response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from jose import jwt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get("sub")

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/")
async def chat(req: ChatRequest, user: str = Depends(get_current_user)):
    response = get_response(req.query, user)
    return {"response": response}
