from xmlrpc.client import Boolean
from sqlalchemy.orm import Session
from api.repositories import todo as todo_repository
from api.models.todo import ToDo


def get_all_to_do(db: Session, current_user_id:int):
    try:
        return todo_repository.get_all_to_do(db,current_user_id)
    except Exception as err:
        raise err


def get_to_do_by_id(db: Session, todo_id: int,current_user_id:int):
    try:
        return todo_repository.get_to_do_by_id(db, todo_id,current_user_id)
    except Exception as err:
        raise err


def check_if_to_do_exist(db: Session, todo_id: int,current_user_id:int) -> Boolean:
    try:
        if not(todo_repository.get_to_do_by_id(db, todo_id,current_user_id=current_user_id)):
            return False
        return True
    except Exception as err:
        raise err


def create_to_do(db: Session, todo: ToDo,current_user_id:int):
    try:
        return todo_repository.create_to_do(db, todo,current_user_id)
    except Exception as err:
        raise err


def update_to_do(db: Session, todo_id: int, todo: ToDo,current_user_id:int):
    try:
        todo_repository.update_to_do(db, todo_id, todo,current_user_id)
    except Exception as err:
        raise err


def delete_to_do(db: Session, todo_id: int,current_user_id:int):
    return todo_repository.delete_to_do(db, todo_id,current_user_id)
