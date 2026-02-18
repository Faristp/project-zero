from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/{item_number}")
async def get_item(item_number:int):
    return {"item ":item_number}