from sqlalchemy.orm import Session
from api import schemas
from api.models.todo import ToDo


def get_all_to_do(db: Session,current_user_id:int):
    try:
        return db.query(schemas.Todo).filter(schemas.Todo.user_id == current_user_id).all()
    except Exception as err:
        raise err


def get_to_do_by_id(db: Session, todo_id: int,current_user_id:int):
    try:
        return db.query(schemas.Todo).filter(schemas.Todo.id == todo_id, 
                                             schemas.Todo.user_id == current_user_id).first()
    except Exception as err:
        raise err


def create_to_do(db: Session, todo: ToDo,current_user_id:int):
    try:
        db_todo = schemas.Todo(name=todo.name, description=todo.description,user_id=current_user_id)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo
    except Exception as err:
        raise err


def update_to_do(db: Session, todo_id: int, todo: ToDo,current_user_id:int):
    try:
        db.query(schemas.Todo).filter(
            schemas.Todo.id == todo_id).update({
                schemas.Todo.description: todo.description,
                schemas.Todo.name: todo.name,
                schemas.Todo.user_id:current_user_id})
        db.commit()
        return get_to_do_by_id(db, todo_id,current_user_id=current_user_id)
    except Exception as err:
        raise err


def delete_to_do(db: Session, todo_id: int,current_user_id:int):
    try:
        db.query(schemas.Todo).filter(
            schemas.Todo.id == todo_id,
            schemas.Todo.user_id == current_user_id).delete(synchronize_session=False)
        db.commit()
    except Exception as err:
        raise err
