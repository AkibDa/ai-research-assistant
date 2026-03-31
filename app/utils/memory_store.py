#app/utils/memory_store.py

from app.db import SessionLocal, Message


def save_message(user, role, content):
  db = SessionLocal()
  try:
    msg = Message(user=user, role=role, content=content)
    db.add(msg)
    db.commit()
  except Exception:
    db.rollback()
    raise
  finally:
    db.close()

def get_user_messages(user):
    db = SessionLocal()
    msgs = (
      db.query(Message)
      .filter(Message.user == user)
      .order_by(Message.id.asc())
      .all()
    )
    db.close()
    return [{"role": m.role, "content": m.content} for m in msgs]
