"""This module includes api endpoints for user."""

from fastapi import APIRouter, status, Depends

from schemas.user import User, UserCreate
from dependencies import verify_token


router = APIRouter()


@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user_input: UserCreate):
    """Create a new user in the database."""
    print(user_input)
    return {"test": user_input}


@router.get(
    "/user/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)]
)
async def get_user(user_id: int):
    """Retrieve a user by provided user_id."""
    from datetime import datetime
    from uuid import uuid4
    return {
        "account_id": uuid4(),
        "created": datetime.now(),
        "first_name": None,
        "last_name": "test"
    }


@router.patch(
    "/user/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)]
)
async def update_user(user_id: str):
    """Update a user by provided user_id."""
    return {"test": user_id}
