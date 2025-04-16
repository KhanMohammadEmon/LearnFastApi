from fastapi import FastAPI, Body
from typing import Annotated
from models.user import userModel, userModel2, userModel3
app = FastAPI()


@app.put("/", tags=["Update user 1"])
async def update_user_1(request_body: Annotated[userModel, Body(example={
    "name": "John Doe",
})]):
    print(request_body)
    pass


@app.put("/2", tags=["Update user 2"])
async def update_user_2(request_body: Annotated[userModel2, Body()]):
    print(request_body)
    pass


@app.put("/3", tags=["Update user 2"])
async def update_user_3(request_body: Annotated[userModel3, Body()]):
    print(request_body)
    pass


@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}


@app.put("/update", tags=["Update user use OPENAPI"])
async def update_user4(request_body: Annotated[userModel, Body(
    openapi_examples={
        "normal": {
            "summary": "A normal example",
            "description": "A **normal** item works correctly.",
            "value": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            },
        },
        "converted": {
            "summary": "An example with converted data",
            "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
            "value": {
                "name": "Bar",
                "price": "35.4",
            },
        },
        "invalid": {
            "summary": "Invalid data is rejected with an error",
            "value": {
                "name": "Baz",
                "price": "thirty five point four",
            },
        },
    },
)]):
    print(request_body)
    pass
