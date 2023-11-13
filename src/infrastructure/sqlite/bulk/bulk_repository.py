from typing import Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.session import Session

from src.domain.bulk.bulk import Bulk


from src.domain.bulk.bulk_repository import BulkRepository
from src.usecase.bulk.bulk_command_usecase import BulkCommandUseCaseUnitOfWork
from .bulk_dto import BulkDTO


class BulkRepositoryImpl(BulkRepository):
    """BulkRepositoryImpl implements CRUD operations related Bulk entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_status(self, status: int) -> Optional[list[Bulk]]:
        try:
            bulk_dtos = self.session.query(BulkDTO).filter_by(status=status).all()
        except NoResultFound:
            return None
        except:
            raise

        if len(bulk_dtos) == 0:
            return []

        return list(map(lambda bulk_dto: bulk_dto.to_read_model(), bulk_dtos))

    def create(self, bulk: Bulk):
        bulk_dto = BulkDTO.from_entity(bulk)
        try:
            self.session.add(bulk_dto)
        except:
            raise

    def find_by_id(self, idbulk: int) -> Optional[Bulk]:
        try:
            bulk_dto = self.session.query(BulkDTO).filter_by(idbulk=idbulk).one()
        except NoResultFound:
            return None
        except:
            raise

        return bulk_dto.to_entity()


class BulkCommandUseCaseUnitOfWorkImpl(BulkCommandUseCaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        bulk_repository: BulkRepository,
    ):
        self.session: Session = session
        self.bulk_repository: BulkRepository = bulk_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
