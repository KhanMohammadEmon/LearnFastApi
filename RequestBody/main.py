from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from schemas.userSchema import UserSchema
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.post("/", tags = ["create user"])
async def store(user: UserSchema) -> UserSchema:
    encode = jsonable_encoder(user)
    print(encode)
    return JSONResponse(status_code = status.HTTP_201_CREATED, content = encode)

@app.get("/")
async def index():
    return {
        "Hello":"World"
    }
