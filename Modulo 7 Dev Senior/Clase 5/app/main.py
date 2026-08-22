from fastapi import FastAPI
from routes import auth_routes
from core.logger import init_logger
from database.session import engine, Base
from models import user_task

app = FastAPI()

Base.metadata.create_all(bind=engine)

init_logger()

app.include_router(auth_routes.router)
