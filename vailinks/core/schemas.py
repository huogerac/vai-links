from typing import List, Optional

from ninja import Schema


class LinkSchemaIn(Schema):
    description: str


class LinkSchema(Schema):
    id: Optional[int]
    description: str
    keyword: str
    link: str


class ListLinksSchema(Schema):
    links: List[LinkSchema]
