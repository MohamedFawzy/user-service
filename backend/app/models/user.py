from typing import Optional

from pydantic import Field
from app.models.core import CoreModel, IDModelMixin


class UserBase(CoreModel):
    """
    All common characteristics of our user model
    """

    first_name: Optional[str] = Field(..., example="Mohamed")
    last_name: Optional[str] = Field(..., example="Fawzy")
    email: str = Field(..., example="example@email.com")
    password: str = Field(..., example="pass213234")


class userCreate(UserBase):
    first_name: str
    last_name: str


class UserInDB(IDModelMixin, UserBase):
    first_name: str
    last_name: str
    email: str
    is_active: str


class UserPublic(IDModelMixin):
    first_name: str
    last_name: str
    email: str
