### Users DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message" : "No encontrado"}})


@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

# Path
@router.get("/{id}")
async def user(id : str):
    return searchUser("_id", ObjectId(id))     

# Query
@router.get("/")
async def user(id : str):
    return searchUser("_id", ObjectId(id))

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user : User):
    if type(searchUser("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Usuario ya está registrado")
    
    user_dict = dict(user)
    del user_dict["id"] # el id lo genera mongodb
    
    id = db_client.users.insert_one(user_dict).inserted_id
    
    new_user = user_schema(db_client.users.find_one({"_id" : id})) # mongo db crea el id como _id
    
    return User(**new_user) # lo devuelve como objeto User

@router.put("/", response_model=User) # para actualizar el usuario completo
async def user(user: User):
        
    user_dict = dict(user)
    del user_dict["id"]
            
    try:
        db_client.users.find_one_and_replace(
            {"_id" : ObjectId(user.id)}, user_dict)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Usuario no actualizado")
        
    return searchUser("_id", ObjectId(user.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id : str): 
    
    found = db_client.users.find_one_and_delete({"_id" : ObjectId(id)})

            
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No se ha eliminado el usuario")


def searchUser(field : str, key):
    try:
        user = db_client.users.find_one({field : key})
        return User(**user_schema(user))
    except:
        return {"error" : "No se ha encontrado el usuario"}  