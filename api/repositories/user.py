from sqlalchemy.orm import Session
from api import schemas
from api.models.user import CreateUser, User as UserModel


def get_user_by_username(db: Session, username: str):
    try:
        user_db = db.query(schemas.User).filter(schemas.User.username == username).first()
        return UserModel( id = user_db.id,
                          username=user_db.username,
                          user_password=user_db.user_password,
                          email=user_db.email,
                          full_name=user_db.full_name)
    except Exception as err:
        raise err


# TODO: Parece que esta consulta no funciona correctamente.
def get_user_by_username_and_password(db: Session, username: str, password: str):
    try:
        return db.query(schemas.User).filter(schemas.User.username == username,
                                             schemas.User.user_password == password).first()
    except Exception as err:
        raise err


def create_user(db: Session, user_to_create: CreateUser):
    try:
        db_user = schemas.User(username=user_to_create.username,
                               user_password=user_to_create.user_password,
                               email=user_to_create.email,
                               full_name=user_to_create.full_name,
                               disabled=False)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return user_to_create
    except Exception as err:
        raise err
