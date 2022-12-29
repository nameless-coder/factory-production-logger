from typing import Optional
from datetime import datetime

from beanie import Document
from pydantic import BaseModel


class ProductionRun(Document):
    pr_id: str
    name: str
    description: Optional[str]
    started: datetime = None

    class Config:
        schema_extra = {
            "example": {
                "pr_id": "FA-01",
                "name": "1st production run",
                "description": "Testing the equipment!",
                "started": "2022-12-23T10:20:30.400+02:00"
            }
        }

    class Settings:
        name = "production_runs"


class ProductionRunUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Framing material",
                "description": "Changed gears"
            }
        }
