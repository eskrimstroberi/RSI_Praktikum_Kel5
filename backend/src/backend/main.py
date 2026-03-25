from fastapi import FastAPI
from backend.schemas.item import ItemCreate, ItemUpdate, ItemBase
from backend.services.item import (
    get_all_item,
    get_item,
    add_item,
    remove_item,
    update_item,
)

app = FastAPI()


@app.get("/item")
def read_all_item():
    return get_all_item()


@app.get("/item/{item_id}")
def read_item(item_id: int):
    return get_item(item_id)


@app.post("/item")
def create_item(item_in: ItemCreate):
    return add_item(item_in)


@app.put("/item/{item_id}", response_model=ItemBase)
def patch_item(item_id: int, item_in: ItemUpdate):
    updated_item = update_item(item_id, item_in)
    updated_item = updated_item.model_dump()
    return {
        "old_item": {"id": item_id, "name": item_in.model_dump()["name"]},
        "updated_item": {"id": updated_item["id"], "name": updated_item["name"]},
    }


@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    deleted_item = remove_item(item_id)
    return {
        "message": f"Item with id: {deleted_item.id} and name: {deleted_item.name} was successfully deleted."
    }
