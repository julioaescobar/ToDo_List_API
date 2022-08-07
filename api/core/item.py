from sqlalchemy.orm import Session

from api.repositories import item as item_repository
from api.models.item import Item


def get_items_by_todo_id(db: Session, todo_id: int):
    return item_repository.get_items_by_todo_id(db, todo_id)


def get_item(db: Session, todo_id: int, item_id: int):
    return item_repository.get_item(db, todo_id, item_id)


def create_item(db: Session, todo_id: int, item_to_create: Item):
    return item_repository.create_item(db, todo_id, item_to_create)


def update_item(db: Session, todo_id: int, item_id: int, item: Item):
    return item_repository.update_item(db, todo_id, item_id, item)


def delete_item(db: Session, todo_id: int, item_id: int):
    return item_repository.delete_item(db, todo_id, item_id)
