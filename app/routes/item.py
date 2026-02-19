from fastapi import APIRouter,Query
from typing import Annotated

from app.models.item import Item
from app.services import item as item_service
router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/{item_number}")
async def get_item(item_number:int, q:str | None = None, short:bool = False):
    return item_service.get_item(item_number,q,short)

@router.get("/")
async def get_items(skip:int = 0, limit: int = 10):
    return item_service.get_items(skip,limit)

@router.post("/")
async def create_item(item:Item):
    return item_service.add_item(item)

@router.put("/{itemId}")
async def update_item(itemId:int,item:Item, q:Annotated[str | None , Query(max_length=5)]= None):
    return item_service.update_item(itemId,item,q)

