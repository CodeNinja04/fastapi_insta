from fastapi import FastAPI
from db.database import engine
from db import models
from routers import user

app= FastAPI()
app.include_router(user.router)
@app.get("/")
def hello():
    return "Hello"

models.Base.metadata.create_all(engine)