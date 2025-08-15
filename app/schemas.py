from pydantic import BaseModel, ConfigDict, field_serializer
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    completed: bool = False

class TodoCreate(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(TodoBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
    updated_at: datetime

    @field_serializer('id')
    def serialize_id(self, id: int, _info):
        return str(id)

    @field_serializer('created_at', 'updated_at')
    def serialize_datetime(self, dt: datetime, _info):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
