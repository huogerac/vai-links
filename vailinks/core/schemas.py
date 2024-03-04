from typing import List, Optional

from ninja import Schema
from pydantic import validator


class LinkSchemaIn(Schema):
    description: str

    @validator("description")
    def valid_description(cls, description):
        if description and len(description) <= 2:
            raise ValueError("It must be at least 3 characteres long.")
        return description


class LinkSchema(Schema):
    id: Optional[int]
    description: str
    link: str


class ListLinksSchema(Schema):
    links: List[LinkSchema]
