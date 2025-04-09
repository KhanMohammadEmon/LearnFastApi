from fastapi import FastAPI


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root(skip: int = 0, limit: int = 10):

    items = fake_items_db[skip: skip + limit]
    return [items]
