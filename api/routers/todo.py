from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter

from api.repositories import todo as todo_repository
from api.database import get_db
from api.models.todo import ToDo

router = APIRouter(
    prefix="/api/todos"
)

@router.get("",description="Devuelve todas las listas de tareas")
def get_all_to_do(db: Session = Depends(get_db)):
    return todo_repository.get_all_to_do(db)

@router.get("/{todo_id}",description="Devuelve un to do list")
def get_to_do(todo_id:int,db: Session = Depends(get_db)):
    return  todo_repository.get_to_do_by_id(db,todo_id=todo_id)

@router.post("/",description="Crea un to do list")
def create_to_do(todo:ToDo,db: Session = Depends(get_db)):
    return todo_repository.create_to_do(db,todo=todo)

@router.put("/{todo_id}",description="Actualiza un to do list")
def update_to_do(todo:ToDo,todo_id: int, db: Session = Depends(get_db)):
    return todo_repository.update_to_do(db,todo_id,todo)  

@router.delete("/{todo_id}",description="Elimina un to do list")
def delete_to_do(todo_id:int, db:Session = Depends(get_db)):
    return todo_repository.delete_to_do(db,todo_id)