from typing import Iterator, List, Optional, Tuple

from traxion.models.v1.vehicles import VehicleModel
from traxion.services.base_services.base_service import BaseService


class VehicleService(BaseService[VehicleModel]):
    __entity_model__ = VehicleModel

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
    ) -> Tuple[int, Iterator[VehicleModel]]:
        count, query_result = self._query_paginated(
            page=page, limit=limit, and_conditions=conditions, sort=sort
        )
        return count, map(lambda x: VehicleModel(**x), query_result)
