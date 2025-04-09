from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from enum import Enum
app = FastAPI()


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"


@app.get("/user/{role}")
async def user(role: Role):

    if role is role.ADMIN:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "User": "Emon",
                "Role": "Admin",
            }
        )

    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "User": "Emon",
                "Role": "User",
            }
        )


@app.get("/")
async def root():
    return {"message": "Hello World"}
