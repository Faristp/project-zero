from app.db.items import fake_items_db

def get_items(skip:int,limit:int):
    return fake_items_db[skip:skip+limit]

def get_item(item_number:int, q:str | None = None, short:bool = False):
    item = {"item_number":item_number}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description": "This is wonderfull item with long description"})
    return item
