from fastapi import APIRouter, Path

from model import Item, ItemItem

item_router = APIRouter()

item_list = []


@item_router.post("/item")
async def add_item(item: Item) -> dict:
    item_list.append(item)
    return {
        "message": "Todo added successfully."
    }


@item_router.get("/item")
async def retrieve_item() -> dict:
    return {
        "items": item_list
    }


@item_router.get("/item/{item_id}")
async def get_single_item(item_id: int = Path(..., title="The ID of the item to retrieve.")) -> dict:
    for item in item_list:
        if item.id == item_id:
            return {
                "item": item
            }
    return {
        "message": "Item with supplied ID doesn't exist."
    }


@item_router.put("/item/{item_id}")
async def update_item(item_data: ItemItem, item_id: int = Path(..., title="The ID of the item to be updated.")) -> dict:
    for item in item_list:
        if item.id == item_id:
            item.item = item_data.item
            return {
                "message": "Item updated successfully."
            }
    return {
        "message": "Item with supplied ID doesn't exist."
    }


@item_router.delete("/item/{item_id}")
async def delete_single_item(item_id: int) -> dict:
    for index in range(len(item_list)):
        item = item_list[index]
        if item.id == item_id:
            item_list.pop(index)
            return {
                "message": "Item deleted successfully."
            }
    return {
        "message": "Item with supplied ID doesn't exist."
    }


@item_router.delete("/item")
async def delete_all_items() -> dict:
    item_list.clear()
    return {
        "message": "Items deleted successfully."
    }
