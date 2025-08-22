from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    completed: bool = False

class TodoCreate(BaseModel):
    title: str

    @validator('title', pre=True)
    def validate_title(cls, v):
        if not isinstance(v, str):
            raise ValueError('title must be a string')
        if len(str(v).strip()) == 0:
            raise ValueError('title cannot be empty')
        return v

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        d['id'] = str(d['id'])
        d['created_at'] = d['created_at'].strftime("%Y-%m-%d %H:%M:%S")
        d['updated_at'] = d['updated_at'].strftime("%Y-%m-%d %H:%M:%S")
        return d
