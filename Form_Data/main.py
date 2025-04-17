from fastapi import FastAPI,Form,Request
from typing import Annotated

app = FastAPI()



@app.post("/login")
async def login(username: Annotated[str|None, Form()]=None, password: Annotated[str|None, Form()]=None):
    print(f"username: {username}, password: {password}")
    return {
        "username": {username},
        "password": {password},
    }


@app.post("/login2")
async def login2(req:Request):
    data = await req.form()
    dict_data = dict(data)
    print(f"username: {dict_data['username']}, password: {dict_data['password']}")
    return {
        "username": {dict_data['username']},
        "password": {dict_data['password']},
    }


@app.get("/")
def read_root():
    return {"Hello": "World"}