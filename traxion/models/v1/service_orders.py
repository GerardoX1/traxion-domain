from enum import Enum
from time import time
from typing import Literal

from pydantic import Field, PositiveInt

from traxion.models.base_models.base_model import BaseModel
from traxion.models.base_models.updatable_model import UpdatableModel


class ServiceType(str, Enum):
    PREVENTIVE = "PREVENTIVE"
    CORRECTIVE = "CORRECTIVE"
    SCHEDULED = "SCHEDULED"


class ServiceStatusType(str, Enum):
    PREVENTIVE = "PREVENTIVE"
    CORRECTIVE = "CORRECTIVE"
    SCHEDULED = "SCHEDULED"


class ServiceOrderModel(BaseModel, UpdatableModel):
    __collection_name__: str = "service_orders"
    version: Literal["1.0.0"] = "1.0.0"
    updated_at: PositiveInt = Field(default_factory=lambda: round(time() * 1000))
    vehicle_id: str
    service_type: list[ServiceType]
    description: str
    status: list[ServiceStatusType]
