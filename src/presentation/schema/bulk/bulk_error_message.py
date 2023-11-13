from pydantic import BaseModel, Field

from src.domain.bulk.bulk_exception import BulkIdAlreadyExistsError


class ErrorMessageBulkIdAlreadyExists(BaseModel):
    detail: str = Field(example=BulkIdAlreadyExistsError.message)