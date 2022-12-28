from datetime import datetime
from pydantic import BaseModel


class ProductionRun(BaseModel):
    id: int
    name: str
    dt: datetime = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Example Schema!",
                "dt": '2022-12-23T10:20:30.400+02:00'
            }
        }


class ProductionRunItem(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Framing material"
            }
        }
