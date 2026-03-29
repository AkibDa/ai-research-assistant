from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.auth_service import *
from app.db import SessionLocal, User as DBUser

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: User):
    db = SessionLocal()

    existing = db.query(DBUser).filter(DBUser.username == user.username).first()
    if existing:
        db.close()
        raise HTTPException(status_code=400, detail="User exists")

    hashed = hash_password(user.password)

    new_user = DBUser(username=user.username, password=hashed)
    db.add(new_user)
    db.commit()
    db.close()

    return {"message": "User registered"}

@router.post("/login")
def login(user: User):
    db = SessionLocal()

    db_user = db.query(DBUser).filter(DBUser.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password):
        db.close()
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.username})
    db.close()

    return {"access_token": token}