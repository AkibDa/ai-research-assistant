# app/routes/upload.py

from fastapi import APIRouter, UploadFile, Depends
from app.services.auth_service import get_current_user
from app.db import SessionLocal, Document

router = APIRouter()

@router.post("/")
async def upload(file: UploadFile, user: str = Depends(get_current_user)):
    content = await file.read()
    text = content.decode("utf-8")

    db = SessionLocal()
    doc = Document(
        username=user,
        filename=file.filename,
        content=text
    )
    db.add(doc)
    db.commit()
    db.close()

    return {"message": "File uploaded successfully"}
