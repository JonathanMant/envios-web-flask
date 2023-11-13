from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.bulk.bulk import Bulk
from src.infrastructure.sqlite.database import Base
from src.usecase.bulk.bulk_query_model import BulkReadModel


class BulkDTO(Base):
    __tablename__ = 'bulk'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    idbulk: Mapped[int] = mapped_column(unique=True, nullable=False)
    status: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    retries: Mapped[int] = mapped_column(nullable=True)

    def to_entity(self) -> Bulk:
        return Bulk(
            bulk_id=self.id,
            idbulk=self.idbulk,
            status=self.status,
            name=self.name,
            retries=self.retries,
        )

    def to_read_model(self) -> BulkReadModel:
        return BulkReadModel(
            bulk_id=self.id,
            idbulk=self.idbulk,
            status=self.status,
            name=self.name,
            retries=self.retries,
        )

    @staticmethod
    def from_entity(bulk: Bulk) -> "BulkDTO":
        return BulkDTO(
            id=bulk.bulk_id,
            idbulk=bulk.idbulk,
            status=bulk.status,
            name=bulk.name,
            retries=bulk.retries,
        )
