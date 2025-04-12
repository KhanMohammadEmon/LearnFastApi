from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.user import UserModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.put("/",tags=["nasted"])
async def updateUser(request_body: UserModel):
   encoded = jsonable_encoder(request_body)
   print(encoded)
   return JSONResponse(content=encoded, status_code=200)