from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter

from api.core import item
from api.database import get_db
from api.models.item import Item

router = APIRouter(
    prefix="/api/todos"
)


@router.get("/{todo_id}/items", description="Devuelve todos los items de un To Do")
def get_all_items(todo_id: int, db: Session = Depends(get_db)):
    return item.get_items_by_todo_id(db, todo_id)


@router.get("/{todo_id}/items/{item_id}", description="Devuelve un item")
def get_items(todo_id: int, item_id: int, db: Session = Depends(get_db)):
    return item.get_item(db, todo_id, item_id)


@router.post("/{todo_id}/items", description="Create un item en un TODO")
def create_item(todo_id: int, item_to_create: Item, db: Session = Depends(get_db)):
    return item.create_item(db, todo_id, item_to_create)


@router.put("/{todo_id}/items/{item_id}", description="Actualiza un item")
def update_item(todo_id: int, item_id: int, item_to_update: Item, db: Session = Depends(get_db)):
    return item.update_item(db, todo_id, item_id, item_to_update)


@router.delete("/{todo_id}/items/{item_id}", description="Elimina un item de un TODO")
def delete_item(todo_id: int, item_id, db: Session = Depends(get_db)):
    return item.delete_item(db, todo_id, item_id)
