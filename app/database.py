import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, delcarative_base

POSTGRES_USER = os.getenv("POSTGRES_USER", "todo_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "todo_pass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "todo_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autofluse=False, bind=engine)

Base = delcarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        