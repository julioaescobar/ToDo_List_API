from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Response,  status, HTTPException
from api.security.security import oauth2_scheme, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from api.core import user as user_core
from api.database import get_db
from api.models.user import CreateUser
from api.models.token import Token
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta


router = APIRouter()


@router.post("/api/users/create", description="Crea un usuario", status_code=status.HTTP_201_CREATED)
def create_user(user_to_create: CreateUser, response: Response, db: Session = Depends(get_db)):
    try:
        return user_core.create_user(db, user_to_create)
    except Exception as err:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(err)


@router.get("/api/users/me")
async def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = await user_core.get_current_user(db, token)
    return current_user


@router.post("/token", response_model=Token)
async def login_for_access_token(user = Depends(user_core.authenticate_user)):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
