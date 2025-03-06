from abc import ABC, abstractmethod
from typing import Optional


class BaseServiceABC(ABC):
    """Abstract base class for defining a generic service interface."""

    @abstractmethod
    def get(self, document_id: str) -> Optional[object]:
        ...

    @abstractmethod
    def create(self, document_data: object) -> Optional[object]:
        ...

    @abstractmethod
    def update(self, document_data: object) -> Optional[object]:
        ...
