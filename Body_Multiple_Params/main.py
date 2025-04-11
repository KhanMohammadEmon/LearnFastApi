from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Annotated
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()


class User(BaseModel):
    name: str | None = None
    userName: str
    password: str
    age: int | None = 20


@app.put("/{id}", tags=["Get ID"])
async def get_id(id: Annotated[int, Path(title="Path id", ge=1, le=10)], query: Annotated[str, Query(alias="Enter Name", max_length=10, min_length=2)] = None, user: User = None):
    result = {
        "userID": id
    }

    if query:
        result.update({"query": query})

    if user:
        result.update({"user": jsonable_encoder(user)})

    return JSONResponse(content = result, status_code = 200)

