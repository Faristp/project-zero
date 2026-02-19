import random
from typing import Annotated

from app.db.items import data
from app.models.item import Item

def get_item(item_number:int, q:str | None = None, short:bool = False):
    item = {"item_number":item_number}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description": "This is wonderfull item with long description"})
    return item

def add_item(item:Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price+item.tax
        item_dict.update({"item_with_tax":price_with_tax})
    return item_dict

def update_item(itemId:int, item:Item, q:str | None=None):
    item_dict = {"item Id":itemId,**item.model_dump()}
    if q is not None:
        item_dict.update({"q":q}) 
    return item_dict

def read_items(
    id: Annotated[str | None, ()] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}