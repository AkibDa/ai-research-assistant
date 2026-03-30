# app/services/llm_service.py

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from app.utils.memory_store import get_user_messages, save_message
from app.db import SessionLocal, Document

load_dotenv()

llm = ChatGoogleGenerativeAI(
  model="gemini-2.5-flash",
  temperature=1.0,
  max_tokens=None,
  timeout=None,
  max_retries=2,
)

def get_user_context(user: str):
  db = SessionLocal()
  docs = db.query(Document).filter(Document.username == user).all()
  db.close()

  return "\n".join([doc.content for doc in docs])

def get_response(query: str, user: str):
  memory = get_user_messages(user)
  doc_context = get_user_context(user)

  messages = []

  if doc_context:
    messages.append({
      "role": "system",
      "content": f"Use this user document context:\n{doc_context}"
    })

  messages.extend(memory)
  messages.append({"role": "user", "content": query})

  response = llm.invoke(messages)

  save_message(user, "user", query)
  save_message(user, "assistant", response.content)

  return response.content
