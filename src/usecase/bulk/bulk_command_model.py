from pydantic import BaseModel, Field


class BulkCreateModel(BaseModel):
    """BulkCreateModel represents a write model to create a Bulk."""
    status: int = Field(ge=0, example=320)
    name: str = Field(example="Element")
