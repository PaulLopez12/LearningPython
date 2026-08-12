from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "b362b8dbeed9d05c9a4eaa7498c0bb8c6a1db2fb412415df0823a193a99d8ba5"

router  = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username : str
    full_name : str
    email : str
    disable : bool 
    

class UserDB(User):
    password : str


users_db = {
    "mouredev" : {
        "username" : "mouredev",
        "full_name" : "Braismoure",
        "email" : "braismoure@mouredev.com",
        "disable" : False,
        "password" : "$2a$12$RwfKz/Fg0wDREb2fdfz4EOwwwDZDxEF77d5sJwas6eQ1goeuv1Gni"
    },
        "mouredev2" : {
        "username" : "mouredev2",
        "full_name" : "Braismoure2",
        "email" : "braismoure2@mouredev.com",
        "disable" : True    ,
        "password" : "$2a$12$FtPXgIb55LcTNoyRs0Gd7.RdJzh3gRP6X47qHVMT8Vl91eqSa8xdW"
    }
}


def search_user_db(username : str):
    if username in users_db:
        return UserDB(**users_db[username])        


def search_user(username : str):
    if username in users_db:
        return User(**users_db[username])  


async def auth_user(token : str = Depends(oauth2)):
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"WWW-Authenticate" : "Bearer"}) 
    
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
        
        
    except JWTError:
        raise exception
    
    return search_user(username)


async def current_user(user : User = Depends(auth_user)):       
    if user.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo")
        
    return user


@router.post("/jwt_login")
async def login(form : OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="El usuario no es correcto")    

    user = search_user_db(form.username)
    password_bytes = form.password.encode("utf-8")[:72]
    if not crypt.verify(password_bytes, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="La contraseña no es correcta")
    
    expire = datetime.astimezone(datetime.now(), None) + timedelta(minutes=ACCESS_TOKEN_DURATION)
    
    access_token = {"sub" : user.username, "exp" : expire}
    
    return {"access_token" : jwt.encode(access_token, SECRET, algorithm = ALGORITHM), 
            "token_type" : "bearer"}     


@router.get("/jwt_users/jwt_me")
async def me(user : User = Depends(current_user)):
    return user