from abc import abstractmethod, ABC
import random
from typing import Optional, cast

from src.domain.bulk.bulk import Bulk
from src.domain.bulk.bulk_exception import BulkIdAlreadyExistsError
from src.domain.bulk.bulk_repository import BulkRepository
from src.usecase.bulk.bulk_command_model import BulkCreateModel
from src.usecase.bulk.bulk_query_model import BulkReadModel


class BulkCommandUseCaseUnitOfWork(ABC):
    """BulkCommandUseCaseUnitOfWork defines an interface based on Unit of Work pattern."""

    bulk_repository: BulkRepository

    @abstractmethod
    def begin(self):
        ...

    @abstractmethod
    def commit(self):
        ...

    @abstractmethod
    def rollback(self):
        ...


class BulkCommandUseCase(ABC):
    """BulkCommandUseCase defines a command usecase inteface related Bulk entity."""

    @abstractmethod
    def create_bulk(self, data: BulkCreateModel) -> None:
        raise ...


class BulkCommandUseCaseImpl(BulkCommandUseCase):
    """BulkCommandUseCaseImpl implements a command usecases related Bulk entity."""

    def __init__(
            self,
            uow: BulkCommandUseCaseUnitOfWork,
    ):
        self.uow: BulkCommandUseCaseUnitOfWork = uow

    def create_bulk(self, data: BulkCreateModel) -> None:
        try:
            bulk = Bulk(
                idbulk=random.randint(0, 3),
                status=data.status,
                name=data.name,
            )

            self.uow.bulk_repository.create(bulk)
            self.uow.commit()
        except:
            self.uow.rollback()
            raise
