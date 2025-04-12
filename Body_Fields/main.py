from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated
app = FastAPI()


class User(BaseModel):
    name: str | None
    userName: str
    bio: str | None = Field(
        title="user bio",
        max_length=100,
    )
    salary: float = Field(
        ge=1000,

    )
    age: int | None = 20


@app.put("/user/{user_id}", tags=["User"])
async def update_user(userID: int, user: Annotated[User, Body(embed=True)]):
    result = {
        "user_id": userID,
        "user": user
    }

    return result


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello World"}
