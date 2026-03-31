# app/services/llm_service.py

from app.services.agent_service import agent
from app.utils.memory_store import get_user_messages, save_message
from app.db import SessionLocal, Document
from app.utils.parser import normalize_llm_content

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

  state = {
    "messages": messages
  }

  response = agent.invoke(state)

  final_response = normalize_llm_content(response["messages"][-1].content)

  save_message(user, "user", query)
  save_message(user, "assistant", final_response)

  return final_response
