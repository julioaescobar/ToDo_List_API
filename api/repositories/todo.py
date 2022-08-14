from sqlalchemy.orm import Session
from api import schemas
from api.models.todo import ToDo


def get_all_to_do(db: Session):
    try:
        return db.query(schemas.Todo).all()
    except Exception as err:
        raise err


def get_to_do_by_id(db: Session, todo_id: int):
    try:
        return db.query(schemas.Todo).filter(schemas.Todo.id == todo_id).first()
    except Exception as err:
        raise err


def create_to_do(db: Session, todo: ToDo):
    try:
        db_todo = schemas.Todo(name=todo.name, description=todo.description)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo
    except Exception as err:
        raise err


def update_to_do(db: Session, todo_id: int, todo: ToDo):
    try:
        db.query(schemas.Todo).filter(
            schemas.Todo.id == todo_id).update({
                schemas.Todo.description: todo.description,
                schemas.Todo.name: todo.name})
        db.commit()
        return get_to_do_by_id(db, todo_id)
    except Exception as err:
        raise err


def delete_to_do(db: Session, todo_id: int):
    try:
        db.query(schemas.Todo).filter(
            schemas.Todo.id == todo_id).delete(synchronize_session=False)
        db.commit()
    except Exception as err:
        raise err
