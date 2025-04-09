from fastapi import FastAPI


app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user")
async def get_user():
    return {
        "name": "John Doe", 
        "age": 30,
        "email":"john@gmail.com",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        }
	
    }

