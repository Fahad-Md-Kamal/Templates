from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from app.schemas.comments_schema import CommentDB


class PostBase(BaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)


class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostDB(PostBase):
    id: int


class PostPublic(PostDB):
    comments: List[CommentDB]
