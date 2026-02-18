from fastapi import APIRouter
from app.db.items import fake_items_db

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/{item_number}")
async def get_item(item_number:int):
    return {"item ":item_number}

@router.get("/")
async def get_items(skip:int = 0, limit: int = 10):
    return fake_items_db[skip:skip+limit]