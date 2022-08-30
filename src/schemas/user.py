"""This module includes schemas for user."""

import uuid
import datetime
from typing import Union

from pydantic import BaseModel, Field


class User(BaseModel):
    """Model of user creation."""
    account_id: uuid.UUID
    first_name: Union[str, None]
    last_name: Union[str, None]
    created: datetime.datetime


class UserCreate(BaseModel):
    """Model of user creation."""
    monobank_token: str = Field(..., min_length=10)

    class Config:
        """Additional configuration for user create model."""
        anystr_strip_whitespace = True
