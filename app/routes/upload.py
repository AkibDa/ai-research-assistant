from fastapi import APIRouter, UploadFile
from app.services.vector_store import store_document

router = APIRouter()

@router.post("/")
async def upload(file: UploadFile):
    content = await file.read()
    store_document(content)
    return {"message": "File processed"}