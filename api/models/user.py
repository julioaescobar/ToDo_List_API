from typing import Union
from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    user_password: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None

class User(CreateUser):
    id:int