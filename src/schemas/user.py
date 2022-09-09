"""This module includes schemas for user."""

import uuid
import datetime
from typing import Union

from pydantic import BaseModel, Field

from schemas.base import ResponseSchema


class UserSchema(BaseModel):
    """Base model of user entity."""
    id: uuid.UUID
    first_name: Union[str, None]
    last_name: Union[str, None]
    created_date: datetime.datetime

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    """Model of user creation."""
    first_name: Union[str, None]
    last_name: Union[str, None]
    monobank_token: str = Field(..., min_length=10)

    class Config:
        """Additional configuration for user create model."""
        anystr_strip_whitespace = True


class UserResponseSchema(ResponseSchema):
    """Model for user response."""
    data: UserSchema
