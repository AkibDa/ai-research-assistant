from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.auth_service import *

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: User):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User exists")

    hashed = hash_password(user.password)
    fake_users_db[user.username] = hashed
    return {"message": "User registered"}

@router.post("/login")
def login(user: User):
    stored = fake_users_db.get(user.username)

    if not stored or not verify_password(user.password, stored):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token}