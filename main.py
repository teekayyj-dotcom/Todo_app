from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database
import os

# Drop tables if testing (to ensure clean state)
if os.getenv("TESTING"):
    models.Base.metadata.drop_all(bind=database.engine)

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/todos", response_model=schemas.TodoResponse, status_code=201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(database.get_db)):
    return crud.create_todo(db, todo)

@app.get("/todos", response_model=list[schemas.TodoResponse])
def get_todos(db: Session = Depends(database.get_db)):
    return crud.get_todos(db)

@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: str, todo: schemas.TodoUpdate, db: Session = Depends(database.get_db)):
    if not todo.dict(exclude_unset=True):
        raise HTTPException(status_code=422, detail="At least one field must be provided")
    updated = crud.update_todo(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str, db: Session = Depends(database.get_db)):
    success = crud.delete_todo(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
