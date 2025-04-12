from pydantic import BaseModel,HttpUrl
from enum import Enum

class Relation(Enum):
    Mother = "Mother"
    Father = "Father"

class Image(BaseModel):
    url: HttpUrl  
    Name:str| None

class Parents(BaseModel):
    full_name: str | None
    relation:Relation | None = Relation.Mother 
        
        
        
class UserModel(BaseModel):
    name: str | None
    userName: str 
    password: str 
    # skill: set[str] = set()
    reference: Parents 
    
    image: list[Image]
    
