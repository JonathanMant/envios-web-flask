from typing import List

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.session import Session

from src.usecase.bulk.bulk_query_model import BulkReadModel
from src.usecase.bulk.bulk_query_service import BulkQueryService
from .bulk_dto import BulkDTO


class BulkQueryServiceImpl(BulkQueryService):
    """BulkQueryServiceImpl implements READ operations related Bulk entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_status(self, status: int) -> List[BulkReadModel]:
        try:
            bulks_dto = self.session.query(BulkDTO).filter_by(status=status).all()
        except NoResultFound:
            return None
        except:
            raise

        if len(bulks_dto) == 0:
            return []

        return list(map(
            lambda bulk_dto: bulk_dto.to_read_model().to_dict(),
            bulks_dto
        ))
