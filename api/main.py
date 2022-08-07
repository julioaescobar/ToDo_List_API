import api.config
from api.routers import todo, item
from api.database import engine
from api import schemas
from fastapi import FastAPI


schemas.Base.metadata.create_all(bind=engine)

app = FastAPI(
    description="API para la creación de Listados de Tareas (TODO List)",
    version="1.0.0",
    title="TODO API",
    redoc_url=None
)

app.include_router(todo.router)
app.include_router(item.router)
