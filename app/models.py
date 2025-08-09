# Dinh nghia bang Todo

import uuid
from sqlalchemy import Column, String, Boolean, Datetime
from sqlalchemy.sql import func
from .database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    completed =Column(Boolean, default=False)
    created_at =Column(Datetime(timezone=True), server_default=func.now())
    updated_at = Column(Datetime(timezone=True), onupdate=func.now(), server_default=func.now())

