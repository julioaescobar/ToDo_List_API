from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Response,  status, File, UploadFile, Form, BackgroundTasks

from api.database import get_db
from api.core.worker import batch_insert_items, save_temp_file, delete_temp_file
from api.core.todo import check_if_to_do_exist
from api.core import user as user_core

router = APIRouter(
    prefix="/api/load",
    tags=["Batch", "Items"]
)


@router.post("/file/", status_code=status.HTTP_202_ACCEPTED)
def create_item_for_todo_batch(response: Response,
                               background_tasks: BackgroundTasks,
                               db: Session = Depends(get_db),
                               file: UploadFile = File(),
                               todo_id: int = Form(),
                               current_user = Depends(user_core.get_current_user)):
    try:
        if(file.content_type == "text/csv"):
            if(check_if_to_do_exist(db, todo_id)):
                background_tasks.add_task(background_worker, file, db, todo_id)
            else:
                response.status_code = status.HTTP_404_NOT_FOUND
                return {"message": "todo_id not exist."}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": f"File type not allowed: {file.content_type}. Must be a CSV."}
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


def background_worker(file: UploadFile, db: Session, todo_id: int):
    try:
        tmp_path = save_temp_file(file)
        batch_insert_items(db, todo_id, tmp_path)
        delete_temp_file(tmp_path)
    except Exception as err:
        raise err
