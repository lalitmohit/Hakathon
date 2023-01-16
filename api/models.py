from pydantic import BaseModel
from typing import Optional
class User(BaseModel):
    name: str
    email:str
    mobile_number:str
    password:str

class User1(BaseModel):
    email:str
    password:str
class User2(BaseModel):
    email:str

class Index(BaseModel):
    Date:str
    Open:str
    High:str
    Low:str
    Close:str
    AdjClose:str
    Volume:str