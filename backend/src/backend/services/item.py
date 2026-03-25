from fastapi import HTTPException
from backend.schemas.item import ItemBase, ItemCreate, ItemUpdate
from backend.db.item import items_db


def get_all_item():
    return items_db


def get_item(item_id: int):
    item = next((i for i in items_db if i.id == item_id), None)
    if not item:
        raise HTTPException(404, "Item cannot be found.")
    return item


def add_item(item_in: ItemCreate):
    if not items_db:
        new_id = 1
    else:
        new_id = items_db[-1].id + 1
    item_data = item_in.model_dump()
    new_item = ItemBase(id=new_id, **item_data)
    items_db.append(new_item)

    return new_item


def update_item(item_id: int, item_in: ItemUpdate):
    item = next((i for i in items_db if i.id == item_id), None)
    if item is None:
        raise HTTPException(404, "Item cannot not found.")
    update_data = item_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)

    return item


def remove_item(item_id: int):
    global items_db
    item = next((i for i in items_db if i.id == item_id), None)
    if item is None:
        raise HTTPException(404, "Item cannot not found.")
    items_db = [i for i in items_db if i.id != item_id]
    return item
