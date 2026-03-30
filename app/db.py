# app/db.py

from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
  DATABASE_URL,
  connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
)

Base = declarative_base()

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True, nullable=False)
  password = Column(String, nullable=False)


class Message(Base):
  __tablename__ = "messages"

  id = Column(Integer, primary_key=True, index=True)
  user = Column(String, index=True, nullable=False)
  role = Column(String, nullable=False)
  content = Column(Text, nullable=False)


class Document(Base):
  __tablename__ = "documents"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, index=True, nullable=False)
  filename = Column(String, nullable=False)
  content = Column(Text, nullable=False)


Base.metadata.create_all(bind=engine)
