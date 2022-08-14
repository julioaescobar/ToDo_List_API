from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Response,  status
from api.security.security import oauth2_scheme
from api.core import todo as todo_core
from api.core import user as user_core
from api.database import get_db
from api.models.todo import ToDo

router = APIRouter(
    prefix="/api/todos"
    ,tags=["To Do"]
)


@router.get("", description="Devuelve todas las listas de tareas", status_code=status.HTTP_200_OK)
def get_all_to_do(response: Response, 
                  db: Session = Depends(get_db),
                  current_user = Depends(user_core.get_current_user)):
    try:
        return todo_core.get_all_to_do(db)
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


@router.get("/{todo_id}", description="Devuelve un to do list", status_code=status.HTTP_200_OK)
def get_to_do(todo_id: int, 
              response: Response, 
              db: Session = Depends(get_db),
              current_user = Depends(user_core.get_current_user)):
    try:
        todo_to_return = todo_core.get_to_do_by_id(db, todo_id=todo_id)
        if not (todo_to_return):
            response.status_code = status.HTTP_404_NOT_FOUND
        return todo_to_return
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


@router.post("/", description="Crea un to do list", status_code=status.HTTP_201_CREATED)
def create_to_do(todo: ToDo, 
                 response: Response, 
                 db: Session = Depends(get_db),
                 current_user = Depends(user_core.get_current_user)):
    try:
        return todo_core.create_to_do(db, todo=todo)
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


@router.put("/{todo_id}", description="Actualiza un to do list", status_code=status.HTTP_200_OK)
def update_to_do(todo: ToDo, 
                 response: Response, 
                 todo_id: int, 
                 db: Session = Depends(get_db),
                 current_user = Depends(user_core.get_current_user)):
    try:
        if(todo_core.check_if_to_do_exist(db, todo_id)):
            return todo_core.update_to_do(db, todo_id, todo)
        response.status_code = status.HTTP_404_NOT_FOUND
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


@router.delete("/{todo_id}", description="Elimina un to do list", status_code=status.HTTP_200_OK)
def delete_to_do(todo_id: int, 
                 response: Response, 
                 db: Session = Depends(get_db),
                 current_user = Depends(user_core.get_current_user)):
    try:
        if(todo_core.check_if_to_do_exist(db, todo_id)):
            return todo_core.delete_to_do(db, todo_id)
        response.status_code = status.HTTP_404_NOT_FOUND
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)
