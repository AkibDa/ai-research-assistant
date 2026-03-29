from app.db import SessionLocal, Message

def save_message(user, role, content):
    db = SessionLocal()
    msg = Message(user=user, role=role, content=content)
    db.add(msg)
    db.commit()
    db.close()

def get_user_messages(user):
    db = SessionLocal()
    msgs = db.query(Message).filter(Message.user == user).all()
    db.close()
    return [{"role": m.role, "content": m.content} for m in msgs]