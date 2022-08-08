from xmlrpc.client import Boolean
from sqlalchemy.orm import Session

from api.repositories import item as item_repository
from api.models.item import Item


def get_items_by_todo_id(db: Session, todo_id: int):
    try:
        return item_repository.get_items_by_todo_id(db, todo_id)
    except Exception as err:
        raise err


def get_item(db: Session, todo_id: int, item_id: int):
    try:
        return item_repository.get_item(db, todo_id, item_id)
    except Exception as err:
        raise err


def check_if_item_exist(db: Session, todo_id: int, item_id: int) -> Boolean:
    try:
        if not (item_repository.get_item(db, todo_id, item_id)):
            return False
        return True
    except Exception as err:
        raise err


def create_item(db: Session, todo_id: int, item_to_create: Item):
    try:
        return item_repository.create_item(db, todo_id, item_to_create)
    except Exception as err:
        raise err


def update_item(db: Session, todo_id: int, item_id: int, item: Item):
    try:
        return item_repository.update_item(db, todo_id, item_id, item)
    except Exception as err:
        raise err


def delete_item(db: Session, todo_id: int, item_id: int):
    try:
        return item_repository.delete_item(db, todo_id, item_id)
    except Exception as err:
        raise err
