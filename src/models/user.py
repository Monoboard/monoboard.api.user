"""This module includes user database model."""

import uuid
import logging

from sqlalchemy import exc, Column, String, DateTime, func
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID

from models.base import BaseModel, BaseModelMixin
from schemas.user import UserCreateSchema
from exceptions import (
    DBUniqueViolationError,
    DatabaseError,
)
from constants import (
    UNIQUE_VIOLATION_ERROR,
    MONOBANK_TOKEN_KEY
)


LOGGER = logging.getLogger(__name__)


class User(BaseModel, BaseModelMixin):
    """Class that represents User in the database."""
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    monobank_token = Column(String(255), nullable=False, unique=True)  # TODO: hash?
    created_date = Column(DateTime, nullable=False, default=func.now())

    @classmethod
    def create(cls, session: Session, user_input: UserCreateSchema):
        """Create a user in the database."""
        try:
            user = cls(**user_input.dict())
            user = cls.save(session, user)
        except exc.IntegrityError as err:
            if UNIQUE_VIOLATION_ERROR in str(err):
                raise DBUniqueViolationError(duplicate_fields={MONOBANK_TOKEN_KEY: user_input.monobank_token})

            LOGGER.error("Failed to create user: %s. Error: %s", user_input, err)
            raise DatabaseError(message=str(err))

        return user
