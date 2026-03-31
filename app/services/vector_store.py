# app/services/vector_store.py

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import Optional

vector_db: Optional[FAISS] = None

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)

def store_document(text: str):
    global vector_db

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    if vector_db is None:
        vector_db = FAISS.from_texts(chunks, embeddings)
    else:
        vector_db.add_texts(chunks)


def retrieve_similar_docs(query: str, k: int = 3):
    if vector_db is None:
        return []

    return vector_db.similarity_search(query, k=k)
