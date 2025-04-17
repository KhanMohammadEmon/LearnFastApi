from fastapi import FastAPI,Request,Header
from fastapi.responses import RedirectResponse
from typing import Annotated
from models.user import User 

app = FastAPI()
db: list[User]= []

@app.get("/",response_model=list[User])
def read()-> list[User]:
    isEmpty = len(db) == 0
    if isEmpty:
        return RedirectResponse("/new",status_code=302)
    return db

@app.post("/create",tags=["Create User"])
def create(user:User):
    db.append(user)
    return {
        "message": "User create successfully","user": user.dict()
    }
