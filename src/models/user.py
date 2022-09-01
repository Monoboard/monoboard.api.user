"""This module includes user database model."""

import uuid

from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

from models.base import BaseModel


class User(BaseModel):
    """Class that represents User in the database."""
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    monobank_token = Column(String(255), nullable=False, unique=True)  # TODO: hash?
    created_date = Column(DateTime, nullable=False, default=func.now())
