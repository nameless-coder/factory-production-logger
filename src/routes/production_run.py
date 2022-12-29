from typing import List
from datetime import datetime
import pytz

from beanie import PydanticObjectId
from database.connection import Database
from fastapi import APIRouter, Path, HTTPException, status
from models.production_run import ProductionRun, ProductionRunUpdate

production_run_router = APIRouter(
    tags=["ProductionRun"]
)

production_run_list = []
production_run_database = Database(ProductionRun)


@production_run_router.get("/", response_model=List[ProductionRun])
async def retrieve_all_production_runs() -> List[ProductionRun]:
    production_runs = await production_run_database.get_all()
    return production_runs


@production_run_router.get("/{item_id}", response_model=ProductionRun)
async def retrieve_single_production_run(item_id: PydanticObjectId = Path(..., title="The ID of the item to retrieve.")) -> ProductionRun:
    production_run = await production_run_database.get(item_id)
    if not production_run:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Production run with supplied ID does not exist"
        )
    return production_run


@production_run_router.post("/new")
async def create_production_run(body: ProductionRun) -> dict:
    body.started = datetime.now(pytz.timezone('Europe/Riga'))
    new_production_run = await production_run_database.save(body)
    return {
        "message": "Production run created successfully.",
        "pr": new_production_run
    }


@production_run_router.put("/{item_id}", response_model=ProductionRun)
async def update_production_run(item_data: ProductionRunUpdate,
                                item_id: PydanticObjectId = Path(..., title="The ID of the item to be updated.")) -> ProductionRun:
    updated_production_run = await production_run_database.update(item_id, item_data)
    if not updated_production_run:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Production run with supplied ID does not exist"
        )
    return updated_production_run


@production_run_router.delete("/{item_id}")
async def delete_single_production_run(item_id: PydanticObjectId = Path(..., title="The ID of the item to be deleted.")) -> dict:
    production_run = await production_run_database.get(item_id)
    if not production_run:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Production run with supplied ID does not exist"
        )
    await production_run_database.delete(item_id)
    return {
        "message": "Production run deleted successfully."
    }
