from pydantic import BaseModel, Field


class BulkCreateModel(BaseModel):
    """BulkCreateModel represents a write model to create a Bulk."""
    bulk_id: int = Field(ege=0, example=320)
    idbulk: int = Field(ege=0, example=320)
    status: int = Field(ge=0, example=320)
    name: str = Field(example="Element")
    retries: int = Field(ge=0, example=320)
