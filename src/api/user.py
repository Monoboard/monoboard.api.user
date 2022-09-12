"""This module includes api endpoints for user."""

import uuid

from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends

from dependencies import verify_auth, get_database_session
from models.user import User
from schemas.base import ResponseSchema
from schemas.user import UserResponseSchema, UserUpdateSchema, UserCreateSchema
from utils.response import make_response
from constants import (
    DUPLICATE_USER_SUBCODE,
    DATABASE_ERROR_SUBCODE,
    USER_NOT_FOUND_SUBCODE,
)
from exceptions import (
    DatabaseError,
    DBUniqueViolationError,
    DBNoResultFoundError,
)


router = APIRouter()


@router.post(
    "/user",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ResponseSchema, "description": "Database error"},
        409: {"model": ResponseSchema, "description": "Duplicate user"},
        422: {"model": ResponseSchema, "description": "Validation error"},
    },
)
def create_user(user_input: UserCreateSchema, session: Session = Depends(get_database_session)):
    """Create a new user in the database."""
    try:
        user = User.create(session, user_input)
    except DBUniqueViolationError:
        return make_response(
            success=False,
            http_status=status.HTTP_409_CONFLICT,
            subcode=DUPLICATE_USER_SUBCODE,
            message="User with such token already exists",
        )
    except DatabaseError:
        return make_response(
            success=False,
            http_status=status.HTTP_400_BAD_REQUEST,
            subcode=DATABASE_ERROR_SUBCODE,
            message="Failed to create user in the database",
        )

    return UserResponseSchema(
        success=True,
        message="User was successfully created",
        data=user,
    )


@router.get(
    "/user/{user_id}",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_auth)],
    responses={
        400: {"model": ResponseSchema, "description": "Database error"},
        401: {"model": ResponseSchema, "description": "Unauthorized"},
        404: {"model": ResponseSchema, "description": "User not found"},
        422: {"model": ResponseSchema, "description": "Validation error"},
    },
)
def get_user(user_id: uuid.UUID, session: Session = Depends(get_database_session)):
    """Retrieve a user by provided user_id."""
    try:
        user = User.get(session, user_id)
    except DBNoResultFoundError as err:
        return make_response(
            success=False,
            http_status=status.HTTP_404_NOT_FOUND,
            subcode=USER_NOT_FOUND_SUBCODE,
            message="User not found by provided id",
            data=err.search_fields,
        )
    except DatabaseError:
        return make_response(
            success=False,
            http_status=status.HTTP_400_BAD_REQUEST,
            subcode=DATABASE_ERROR_SUBCODE,
            message="Failed to retrieve user from the database",
        )

    return UserResponseSchema(
        success=True,
        message="User was successfully found",
        data=user,
    )


@router.patch(
    "/user/{user_id}",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_auth)],
    responses={
        400: {"model": ResponseSchema, "description": "Database error"},
        401: {"model": ResponseSchema, "description": "Unauthorized"},
        404: {"model": ResponseSchema, "description": "User not found"},
        422: {"model": ResponseSchema, "description": "Validation error"},
    },
)
def update_user(
    user_id: uuid.UUID,
    user_input: UserUpdateSchema,
    session: Session = Depends(get_database_session),
):
    """Update a user by provided user_id."""
    try:
        user = User.update(session, user_id, user_input)
    except DBNoResultFoundError as err:
        return make_response(
            success=False,
            http_status=status.HTTP_404_NOT_FOUND,
            subcode=USER_NOT_FOUND_SUBCODE,
            message="User not found by provided id",
            data=err.search_fields,
        )
    except DatabaseError:
        return make_response(
            success=False,
            http_status=status.HTTP_400_BAD_REQUEST,
            subcode=DATABASE_ERROR_SUBCODE,
            message="Failed to update user in the database",
        )

    return UserResponseSchema(
        success=True,
        message="User was successfully updated",
        data=user,
    )
