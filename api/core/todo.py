from sqlalchemy.orm import Session

from api.repositories import todo as todo_repository
from api.models.todo import ToDo


def get_all_to_do(db: Session):
    return todo_repository.get_all_to_do(db)


def get_to_do_by_id(db: Session, todo_id: int):
    return todo_repository.get_to_do_by_id(db, todo_id)


def create_to_do(db: Session, todo: ToDo):
    return todo_repository.create_to_do(db, todo)


def update_to_do(db: Session, todo_id: int, todo: ToDo):
    todo_repository.update_to_do(db, todo_id, todo)


def delete_to_do(db: Session, todo_id: int):
    return todo_repository.delete_to_do(db, todo_id)
