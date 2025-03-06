from traxion.models.v1.service_orders import ServiceOrderModel
from traxion.services.base_services.base_service import BaseService


class VehicleService(BaseService[ServiceOrderModel]):
    __entity_model__ = ServiceOrderModel

    def __init__(self, repository: object, verbose: bool = False, *args, **kwargs):
        self.__repository__ = repository
        self.__verbose__ = verbose
        super().__init__(*args, **kwargs)
