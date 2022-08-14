from sqlalchemy.orm import Session
from api import schemas
from api.models.item import Item


def get_items_by_todo_id(db: Session, todo_id: int):
    try:
        return db.query(schemas.Item).filter(
            schemas.Item.todo_id == todo_id).all()
    except Exception as err:
        raise err


def get_item(db: Session, todo_id: int, item_id: int):
    try:
        return db.query(schemas.Item).filter(
            schemas.Item.todo_id == todo_id,
            schemas.Item.id == item_id).first()
    except Exception as err:
        raise err


def create_item(db: Session, todo_id: int, item_to_create: Item):
    try:
        db_item = schemas.Item(
            description=item_to_create.description,
            title=item_to_create.title,
            todo_id=todo_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as err:
        raise err


def update_item(db: Session, todo_id: int, item_id: int, item: Item):
    try:
        db.query(schemas.Item).filter(
            schemas.Item.id == item_id,
            schemas.Item.todo_id == todo_id).update({
                schemas.Item.title: item.title,
                schemas.Item.description: item.description})
        db.commit()
        return get_item(db, todo_id, item_id)
    except Exception as err:
        raise err


def delete_item(db: Session, todo_id: int, item_id: int):
    try:
        db.query(schemas.Item).filter(
            schemas.Item.id == item_id,
            schemas.Item.todo_id == todo_id).delete(synchronize_session=False)
        db.commit()
    except Exception as err:
        raise err
