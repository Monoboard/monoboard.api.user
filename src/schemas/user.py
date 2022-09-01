"""This module includes schemas for user."""

import uuid
import datetime
from typing import Union

from pydantic import BaseModel, Field


class User(BaseModel):
    """Base model of user entity."""
    id: uuid.UUID
    first_name: Union[str, None]
    last_name: Union[str, None]
    created_date: datetime.datetime

    # TODO orm mode


class UserCreate(BaseModel):
    """Model of user creation."""
    monobank_token: str = Field(..., min_length=10)

    class Config:
        """Additional configuration for user create model."""
        anystr_strip_whitespace = True
