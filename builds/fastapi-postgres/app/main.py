from fastapi import FastAPI
from app.routes import items, users
from app.database import Base, engine

# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(users.router, prefix="/users", tags=["users"])
