from abc import ABC, abstractmethod
from typing import Optional

from src.domain.bulk.bulk import Bulk


class BulkRepository(ABC):
    """BulkRepository defines a repository interface for Bulk entity"""

    @abstractmethod
    def create(self, bulk: Bulk) -> Optional[Bulk]:
        ...

    @abstractmethod
    def find_by_status(self, status: int) -> Optional[list[Bulk]]:
        ...

    @abstractmethod
    def find_by_name(self, name: str) -> Optional[Bulk]:
        ...
