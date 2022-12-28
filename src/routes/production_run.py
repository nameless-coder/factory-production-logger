from fastapi import APIRouter, Path

from models.production_run import ProductionRun, ProductionRunItem

production_run_router = APIRouter()

production_run_list = []


@production_run_router.post("/productionrun")
async def add_item(item: ProductionRun) -> dict:
    production_run_list.append(item)
    return {
        "message": "Production run added successfully."
    }


@production_run_router.get("/productionrun")
async def retrieve_item() -> dict:
    return {
        "productions_runs": production_run_list
    }


@production_run_router.get("/productionrun/{item_id}")
async def get_single_item(item_id: int = Path(..., title="The ID of the item to retrieve.")) -> dict:
    for item in production_run_list:
        if item.id == item_id:
            return {
                "item": item
            }
    return {
        "message": "Item with supplied ID doesn't exist."
    }


@production_run_router.put("/productionrun/{item_id}")
async def update_item(item_data: ProductionRunItem, item_id: int = Path(..., title="The ID of the item to be updated.")) -> dict:
    for item in production_run_list:
        if item.id == item_id:
            item.name = item_data.name
            return {
                "message": "Item updated successfully."
            }
    return {
        "message": "Item with supplied ID doesn't exist."
    }


@production_run_router.delete("/productionrun/{item_id}")
async def delete_single_item(item_id: int) -> dict:
    for index in range(len(production_run_list)):
        item = production_run_list[index]
        if item.id == item_id:
            production_run_list.pop(index)
            return {
                "message": "Item deleted successfully."
            }
    return {
        "message": "Item with supplied ID doesn't exist."
    }


@production_run_router.delete("/productionrun")
async def delete_all_items() -> dict:
    production_run_list.clear()
    return {
        "message": "Items deleted successfully."
    }
