from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from .post_schema import PostMini


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    posts: list[PostMini]

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None

    class Config:
        from_attributes = True
