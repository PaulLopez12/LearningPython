from pydantic import BaseModel

class User(BaseModel):
    id : str | None = None#mongodb maneja el id como str
    username : str
    email : str
