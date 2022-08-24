from fastapi import File, UploadFile
from sqlalchemy.orm import Session
from api.core.item import create_item
from api.core import todo as todo_core
from api.models.item import Item
from csv import reader
import os


def batch_insert_items(db: Session, todo_id: int, temp_path:str,current_user_id:int):
    try:
        todo_db = todo_core.get_to_do_by_id(db,todo_id,current_user_id)
        print(f"this is the todo: {todo_db}")
        for cols in get_next_line(temp_path):
            if not (len(cols) == 2):
                raise Exception("Incorrect File format.")
            item_to_create = Item(title=cols[0], description=cols[1])
            create_item(db, todo_db.id, item_to_create,current_user_id)
    except Exception as err:
        raise err


def save_temp_file(file: UploadFile = File()):
    try:
        with open(file.filename, mode="wb") as f:
            f.writelines(file.file.readlines())
        return file.filename
    except Exception as err:
        raise err
    finally:
        file.file.close()


def delete_temp_file(file_name: str):
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
    except Exception as err:
        raise err


def get_next_line(temp_path: str):
    try:
        with open(temp_path, mode="+tr") as read_obj:
            for row in reader(read_obj):
                yield row
    except Exception as err:
        raise err
