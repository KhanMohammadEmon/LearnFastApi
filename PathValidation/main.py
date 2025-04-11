from fastapi import FastAPI, Path, Query
from typing import Annotated
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/products/{product_id}", tags=["products"])
async def get_product(product_id: int):
    print(product_id)
    return {"product_id": product_id}


@app.get("/user/{id}", tags=["user"])
async def getUer(id: Annotated[int, Path(title="The ID of the user to get")]):
    result = {
        "id": 1
    }

    if id:
        result.update({"path": id})
    return JSONResponse(content=result, status_code=200)


@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}


@app.get("/post/{id}", tags=["post"])
async def get_post(id: Annotated[int, Path(title="post id",ge=0 ,le=20)], query: Annotated[str|None , Query(alias="query", title="query", description="query")]):
    result = {
        "id": 1
    }
    if id and query:
        result.update({"post_id": id, "query": query})
    return JSONResponse(content=result, status_code=200)
