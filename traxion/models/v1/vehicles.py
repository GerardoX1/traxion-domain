from enum import Enum
from time import time
from typing import Literal

from pydantic import Field, PositiveInt

from traxion.models.base_models.base_model import BaseModel


class StatusVehicle(str, Enum):
    ACTIVE = "ACTIVE"
    DEACTIVE = "DEACTIVE"


class VehicleModel(BaseModel):
    __collection_name__: str = "vehicles"
    version: Literal["1.0.0"] = "1.0.0"
    updated_at: PositiveInt = Field(default_factory=lambda: round(time() * 1000))
    plate_number: str = Field(..., min_length=1, max_length=10)
    brand: str = Field(..., min_length=1, max_length=15)
    model: str = Field(..., min_length=1, max_length=30)
    year: PositiveInt
    mileage: PositiveInt
    status: list[StatusVehicle]
