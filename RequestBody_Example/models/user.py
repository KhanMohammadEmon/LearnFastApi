from pydantic import BaseModel,Field


class userModel(BaseModel):
    name: str| None 
    
    
    
class userModel2(BaseModel):
    name: str | None = Field(
        examples = ["Emon khan"]
    )
    
class userModel3(BaseModel):
    name: str | None 
    model_config = {
        "json_schema_extra": {
           "examples": [
                {
                    "name": "Emon khan",
                },
            ]
        }
        
    }
    
    
