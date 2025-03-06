from traxion.models.v1.vehicles import VehicleModel
from traxion.services.base_services.base_service import BaseService


class VehicleService(BaseService[VehicleModel]):
    __entity_model__ = VehicleModel

    def __init__(self, repository: object, verbose: bool = False, *args, **kwargs):
        self.__repository__ = repository
        self.__verbose__ = verbose
        super().__init__(*args, **kwargs)
