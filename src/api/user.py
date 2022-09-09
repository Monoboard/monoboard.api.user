"""This module includes api endpoints for user."""

from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends

from constants import DUPLICATE_USER_SUBCODE, DATABASE_ERROR_SUBCODE
from exceptions import DatabaseError, DBUniqueViolationError
from dependencies import verify_token, get_database_session
from models.user import User
from schemas.base import ResponseSchema
from schemas.user import UserResponseSchema, UserSchema, UserCreateSchema
from utils.response import make_response


router = APIRouter()


@router.post(
    "/user",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        409: {"model": ResponseSchema, "description": "Duplicate user"},
        500: {"model": ResponseSchema, "description": "Database error"}
    }
)
async def create_user(user_input: UserCreateSchema, session: Session = Depends(get_database_session)):
    """Create a new user in the database."""
    try:
        user = User.create(session, user_input)
    except DBUniqueViolationError:
        return make_response(
            success=False,
            http_status=status.HTTP_409_CONFLICT,
            subcode=DUPLICATE_USER_SUBCODE,
            message="User with such token already exists"
        )
    except DatabaseError:
        return make_response(
            success=False,
            http_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            subcode=DATABASE_ERROR_SUBCODE,
            message="Failed to create user in the database"
        )

    return UserResponseSchema(
        success=True,
        message="User was successfully created",
        data=user,
    )


@router.get(
    "/user/{user_id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)]
)
async def get_user(user_id: int, session: Session = Depends(get_database_session)):
    """Retrieve a user by provided user_id."""
    pass


@router.patch(
    "/user/{user_id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)]
)
async def update_user(user_id: str, session: Session = Depends(get_database_session)):
    """Update a user by provided user_id."""
    pass
