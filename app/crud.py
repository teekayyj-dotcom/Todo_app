from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(
        title=todo.title,
        completed=False
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db: Session):
    return db.query(models.Todo).all()

def get_todo(db: Session, todo_id: str):
    try:
        id_int = int(todo_id)
        return db.query(models.Todo).filter(models.Todo.id == id_int).first()
    except (ValueError, TypeError):
        return None

def update_todo(db: Session, todo_id: str, todo_data: schemas.TodoUpdate):
    try:
        id_int = int(todo_id)
        db_todo = db.query(models.Todo).filter(models.Todo.id == id_int).first()
        if db_todo:
            update_data = todo_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_todo, field, value)
            db.commit()
            db.refresh(db_todo)
        return db_todo
    except (ValueError, TypeError):
        return None

def delete_todo(db: Session, todo_id: str):
    try:
        id_int = int(todo_id)
        db_todo = db.query(models.Todo).filter(models.Todo.id == id_int).first()
        if db_todo:
            db.delete(db_todo)
            db.commit()
            return True
        return False
    except (ValueError, TypeError):
        return False
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return True
    return False
