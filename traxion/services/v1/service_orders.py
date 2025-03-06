from typing import Iterator, List, Optional, Tuple

from traxion.models.v1.service_orders import ServiceOrderModel
from traxion.services.base_services.base_service import BaseService


class ServiceOrderService(BaseService[ServiceOrderModel]):
    __entity_model__ = ServiceOrderModel

    def __init__(self, repository: object, verbose: bool = False, *args, **kwargs):
        self.__repository__ = repository
        self.__verbose__ = verbose
        super().__init__(*args, **kwargs)

    def paginated_query(
        self,
        conditions: List[tuple] = None,
        page: int = 1,
        limit: int = 10,
        sort: Optional[List[Tuple[str, int]]] = None,
    ) -> Tuple[int, Iterator[ServiceOrderModel]]:
        count, query_result = self._query_paginated(
            page=page, limit=limit, and_conditions=conditions, sort=sort
        )
        return count, map(lambda x: ServiceOrderModel(**x), query_result)
