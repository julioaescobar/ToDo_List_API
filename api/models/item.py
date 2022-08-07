from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: str or None = None
