from abc import abstractmethod, ABC
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
    def create_bulk(self, data: BulkCreateModel) -> Optional[BulkReadModel]:
        raise ...


class BulkCommandUseCaseImpl(BulkCommandUseCase):
    """BulkCommandUseCaseImpl implements a command usecases related Bulk entity."""

    def __init__(
        self,
        uow: BulkCommandUseCaseUnitOfWork,
    ):
        self.uow: BulkCommandUseCaseUnitOfWork = uow

    def create_bulk(self, data: BulkCreateModel) -> Optional[BulkReadModel]:
        try:
            bulk = Bulk(
                bulk_id=data.bulk_id,
                idbulk=data.idbulk,
                status=data.status,
                name=data.name,
                retries=data.retries,
            )

            existing_bulk = self.uow.bulk_repository.find_by_id(data.idbulk)
            if existing_bulk is not None:
                raise BulkIdAlreadyExistsError

            self.uow.bulk_repository.create(bulk)
            self.uow.commit()

            created_bulk = self.uow.bulk_repository.find_by_id(data.idbulk)
        except:
            self.uow.rollback()
            raise

        return BulkReadModel.from_entity(cast(Bulk, created_bulk))
