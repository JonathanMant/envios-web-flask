from abc import ABC, abstractmethod
from typing import Optional

from .bulk_query_model import BulkReadModel
from .bulk_query_service import BulkQueryService
from ...domain.bulk.bulk_exception import BulksNotFoundError


class BulkQueryUseCase(ABC):
    """BulkQueryUseCase defines a query usecase inteface related Bulk entity."""

    @abstractmethod
    def fetch_bulks_by_status(self, status: int) -> Optional[list[BulkReadModel]]:
        """fetch_bulks_by_id fetches some bulks by id."""
        raise NotImplementedError


class BulkQueryUseCaseImpl(BulkQueryUseCase):
    """BulkQueryUseCaseImpl implements a query usecases related Bulk entity."""

    def __init__(self, bulk_query_service: BulkQueryService):
        self.bulk_query_service: BulkQueryService = bulk_query_service

    def fetch_bulks_by_status(self, status: int) -> Optional[list[BulkReadModel]]:
        """fetch_bulks_by_id fetches some bulks by status."""
        try:
            bulks = self.bulk_query_service.find_by_status(status)
            if bulks is None:
                raise BulksNotFoundError
        except:
            raise

        return bulks
