from fastapi import APIRouter,Query, Path
from typing import Annotated

from pydantic import AfterValidator
from app.utilities.validator import check_valid_id
from app.models.item import Item
from app.services import item as item_service
router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/")
async def read_items(id: Annotated[str | None ,AfterValidator(check_valid_id)] = None):
    return item_service.read_items(id)

@router.get("/{item_number}")
async def get_item(item_number:Annotated[int,Path(title="The Id of the item to get")], q:Annotated[str | None, Query(alias="item-query")] = None, short:bool = False):
    return item_service.get_item(item_number,q,short)

@router.post("/")
async def create_item(item:Item):
    return item_service.add_item(item)

@router.put("/{itemId}")
async def update_item(itemId:int,item:Item, q:Annotated[str | None , Query(max_length=5)]= None):
    return item_service.update_item(itemId,item,q)

