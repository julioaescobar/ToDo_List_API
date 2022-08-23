from sqlalchemy.orm import Session
from api.repositories import user as user_repository
from api.models.user import CreateUser
from api.security.security import verify_password, ALGORITHM, SECRET_KEY, get_password_hash
from fastapi import status, HTTPException,Depends
from jose import jwt, JWTError
from api.models.token import TokenData
from fastapi.security import OAuth2PasswordRequestForm
from api.database import get_db


def check_if_user_exist(db: Session, username: str):
    try:
        if not(user_repository.get_user_by_username(db, username)):
            return False
        return True
    except Exception as err:
        raise err


def create_user(db: Session, user_to_create: CreateUser):
    try:
        user_to_create.user_password = get_password_hash(
            user_to_create.user_password)
        return user_repository.create_user(db, user_to_create)
    except Exception as err:
        raise err


async def get_current_user(db: Session, token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = user_repository.get_user_by_username(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user


def authenticate_user(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_repository.get_user_by_username(db, form_data.username)
    if not user:
        return False
    if not verify_password(form_data.password,user.user_password):
        return False
    return user
