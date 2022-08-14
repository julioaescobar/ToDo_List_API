from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, status, Response

from api.core import item as item_core
from api.core import user as user_core
from api.database import get_db
from api.models.item import Item

router = APIRouter(
    prefix="/api/todos",
    tags=["Items"]
)


@router.get("/{todo_id}/items", description="Devuelve todos los items de un To Do", status_code=status.HTTP_200_OK)
def get_all_items(todo_id: int, 
                  response: Response, 
                  db: Session = Depends(get_db),
                  current_user = Depends(user_core.get_current_user)):
    try:
        return item_core.get_items_by_todo_id(db, todo_id)
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


@router.get("/{todo_id}/items/{item_id}", description="Devuelve un item", status_code=status.HTTP_200_OK)
def get_items(todo_id: int, 
              item_id: int, 
              response: Response, 
              db: Session = Depends(get_db),
              current_user = Depends(user_core.get_current_user)):
    try:
        item_to_return = item_core.get_item(db, todo_id, item_id)
        if not (item_to_return):
            response.status_code = status.HTTP_404_NOT_FOUND
        return item_to_return
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


@router.post("/{todo_id}/items", description="Create un item en un TODO", status_code=status.HTTP_201_CREATED)
def create_item(todo_id: int, 
                item_to_create: Item, 
                response: Response, 
                db: Session = Depends(get_db),
                current_user = Depends(user_core.get_current_user)):
    try:
        return item_core.create_item(db, todo_id, item_to_create)
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


@router.put("/{todo_id}/items/{item_id}", description="Actualiza un item", status_code=status.HTTP_200_OK)
def update_item(todo_id: int, 
                item_id: int, 
                response: Response, 
                item_to_update: Item, 
                db: Session = Depends(get_db),
                current_user = Depends(user_core.get_current_user)):
    try:
        if(item_core.check_if_item_exist(db, todo_id, item_id)):
            return item_core.update_item(db, todo_id, item_id, item_to_update)
        response.status_code = status.HTTP_404_NOT_FOUND
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


@router.delete("/{todo_id}/items/{item_id}", description="Elimina un item de un TODO", status_code=status.HTTP_200_OK)
def delete_item(todo_id: int, 
                item_id:int, 
                response: Response, 
                db: Session = Depends(get_db),
                current_user = Depends(user_core.get_current_user)):
    try:
        if(item_core.check_if_item_exist(db, todo_id, item_id)):
            return item_core.delete_item(db, todo_id, item_id)
        response.status_code = status.HTTP_404_NOT_FOUND
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)
