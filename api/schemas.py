from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from api.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, unique=True, index=True)
    description = Column(String)

    items = relationship("Item", back_populates="todo")
    user = relationship("User", back_populates="users")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    todo_id = Column(Integer, ForeignKey("todos.id"))

    todo = relationship("Todo", back_populates="items")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    user_password = Column(String)
    email = Column(String)
    full_name = Column(String)
    disabled = Column(Boolean)

    users = relationship("Todo", back_populates="user")