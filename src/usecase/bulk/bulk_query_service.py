from abc import ABC, abstractmethod
from typing import List

from .bulk_query_model import BulkReadModel


class BulkQueryService(ABC):
    """BulkQueryService defines a query service inteface related Bulk entity."""

    @abstractmethod
    def find_by_status(self, status: int) -> List[BulkReadModel]:
        ...
