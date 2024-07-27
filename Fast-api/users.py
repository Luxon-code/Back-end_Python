from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#entidad user
class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int
    url:str
    
users_list = [User(id=1,name="joseph",surname="trujillo",age=19,url="no tiene"),
         User(id=2,name="jose",surname="tovar",age=13,url="no tiene"),
         User(id=3,name="david",surname="aguilar",age=19,url="no tiene")]

#get

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id:int):
    return search_user(id)
    
    
@app.get("/user/")
async def user(id_user:int):
    return search_user(id_user)
    
def search_user(id:int):
    users = filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "no se ha encontrado al usuario"}
    
#POST 
    
@app.post("/user/")
async def user(user:User):
    if type(search_user(user.id)) == User:
        return {"error": "el usuario ya existe"}
    else:
        users_list.append(user)
        return {"mensaje":"usuario agregado correctamente"}

