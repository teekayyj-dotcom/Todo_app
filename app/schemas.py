from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoResp