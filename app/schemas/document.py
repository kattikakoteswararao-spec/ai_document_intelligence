from typing import Literal

from pydantic import BaseModel, Field


class DocumentMetadata(BaseModel):
    filename: str
    file_type: str
    character_count: int = Field(ge=0)
    word_count: int = Field(ge=0)


class DocumentAnalysis(BaseModel):
    category: Literal[
        "HR",
        "Finance",
        "Legal",
        "Technical",
        "Other",
    ]

    extracted_fields: dict[str, str | int | float | bool | None]

    summary: str