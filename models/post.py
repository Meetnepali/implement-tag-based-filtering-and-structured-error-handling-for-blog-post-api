from typing import List
from pydantic import BaseModel

class BlogPost(BaseModel):
    id: int
    title: str
    tags: List[str]

class TagSearchError(BaseModel):
    detail: str
    invalid_tags: List[str]
