from fastapi import FastAPI, Query
from typing import Annotated
false_data: dict[str, dict[int, str]] = {
    "items": {
        1: "food",
        2: "drink",
        3: "snack",
        4: "fruit",
    }
}

app = FastAPI()


@app.get("/items", tags=["items"])
async def get_items(q: Annotated[str, Query(title = "Get all Item",description="Item get description",alias="Enter str",deprecated = False)] = None):
    print(q)
    if q:
        false_data.update({"new Items": q})
    return false_data


@app.get("/", tags=["health"])
async def root(q: str | None = None):
    print(q)
    return {
        "message": "Hello World",
        "q": q
    }
