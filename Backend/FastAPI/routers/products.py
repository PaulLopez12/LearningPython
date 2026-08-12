from fastapi import APIRouter

router = APIRouter(prefix="/products", responses={404: {"message": "No encontrado"}},
                   tags=["products"])

products_list = ["Prodcuto 1","Prodcuto 2","Prodcuto 3","Prodcuto 4","Prodcuto 5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id : int):
    return products_list[id]