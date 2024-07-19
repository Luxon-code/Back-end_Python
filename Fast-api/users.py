from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#entidad user
class User(BaseModel):
    name:str
    surname:str
    age:int
    url:str
    
users_list = [User(name="joseph",surname="trujillo",age=19,url="no tiene"),
         User(name="jose",surname="tovar",age=13,url="no tiene"),
         User(name="david",surname="aguilar",age=19,url="no tiene")]

@app.get("/users")
async def users():
    return users_list