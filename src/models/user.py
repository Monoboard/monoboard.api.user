"""This module includes user database model."""

import uuid
import logging

from sqlalchemy import exc, Column, String, DateTime, func
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID

from models.base import BaseModel, BaseModelMixin
from schemas.user import UserCreateSchema, UserUpdateSchema
from exceptions import (
    DBUniqueViolationError,
    DBNoResultFoundError,
    DatabaseError,
)
from constants import (
    UNIQUE_VIOLATION_ERROR,
    MONOBANK_TOKEN_KEY,
    ID_KEY,
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
        except exc.SQLAlchemyError as err:
            LOGGER.error("Failed to create user: %s. Error: %s", user_input, err)
            raise DatabaseError(message=str(err))

        return user

    @classmethod
    def get(cls, session: Session, user_id: uuid.UUID):
        """Create a user in the database."""
        try:
            user = session.query(cls).filter(cls.id == user_id).one_or_none()
        except exc.SQLAlchemyError as err:
            LOGGER.error("Failed to retrieve user: %s. Error: %s", user_id, err)
            raise DatabaseError(message=str(err))

        if not user:
            raise DBNoResultFoundError(search_fields={ID_KEY: str(user_id)})

        return user

    @classmethod
    def update(cls, session: Session, user_id: uuid.UUID, user_input: UserUpdateSchema):
        """Update a user in the database."""
        user = cls.get(session, user_id)

        try:
            for key, value in user_input.dict(exclude_unset=True).items():
                setattr(user, key, value)

            user = cls.save(session, user)
        except exc.SQLAlchemyError as err:
            LOGGER.error("Failed to update user %s: %s. Error: %s", user_id, user_input, err)
            raise DatabaseError(message=str(err))

        return user
