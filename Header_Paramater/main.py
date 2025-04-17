from fastapi import FastAPI,Request,Header
from typing import Annotated



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/item")
async def item1(item: str):
    print(item)
    return {"item": item}


@app.get("/headers")
async def get_header(req:Request):
    print(req.headers)
    return {"message":"no"}

@app.get("/header2")
async def get_header2(user: Annotated[str|None,Header(
    convert_underscores=True
)]=None):
    print(user)
    return {"user_agent": user}
