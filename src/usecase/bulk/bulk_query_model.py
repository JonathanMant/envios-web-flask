from pydantic import BaseModel, Field

from src.domain.bulk.bulk import Bulk


class BulkReadModel(BaseModel):
    """BulkReadModel represents data structure as a read model."""

    id: int = Field(ge=0, example=1)
    idbulk: int = Field(ge=0, example=120)
    status: int = Field(ge=0, example=120)
    name: str = Field(example="Element4")
    retries: int = Field(ge=0, example=120)

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(bulk: Bulk) -> "BulkReadModel":
        return BulkReadModel(
            id=bulk.bulk_id,
            idbulk=bulk.idbulk,
            status=bulk.status,
            name=bulk.name,
            retries=bulk.retries,
        )
