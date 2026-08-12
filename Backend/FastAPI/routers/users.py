from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"message" : "No encontrado"}})

# Entidad user
class User(BaseModel):
    id : int
    name : str
    username : str
    url : str
    age : int
    
users_list = [User(id=1,name = "Paul", username = "ZWarkingZ", url = "https://moure.dev", age = 28),
            User(id=2,name ="Anderson", username ="ZMWarkingZ", url = "https://moure.com", age = 27),
            User(id=3,name ="Haakon", username ="Dahlberg", url = "https://Haakon.com", age = 26)]

@router.get("/usersjson")
async def usersjson():
    return [{"name" : "Paul", "username" : "ZWarkingZ", "url" : "https://moure.dev", "age" : 28},
            {"name" : "Anderson", "username" : "ZMWarkingZ", "url" : "https://moure.com", "age" : 27},
            {"name" : "Haakon", "username" : "Dahlberg", "url" : "https://Haakon.com", "age" : 26}]
    
@router.get("/")
async def users():
    return users_list

# Path
@router.get("/{id}")
async def user(id : int):
    return searchUser(id)
 
    
# Query
@router.get("/userquery/")
async def user(id : int):
    return searchUser(id)

@router.post("/user/", response_model=User, status_code=201)
async def user(user : User):
    if type(searchUser(user.id)) == User:
        raise HTTPException(status_code=404,detail="Usuario ya está registrado")
    else:
        users_list.append(user)
        return user

@router.put("/user/") # para actualizar el usuario completo
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
    if not found: 
        raise HTTPException(status_code=404,detail="Usuario no actualizado")
    else:
        return user
    
@router.delete("/user/{id}")
async def user(id : int): 
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            
    if not found:
        raise HTTPException(status_code=404,detail="No se ha eliminado el usuario")

def searchUser(id : int):
    users = filter(lambda user : user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error" : "No se ha encontrado el usuario"}  
    
