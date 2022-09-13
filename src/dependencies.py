"""This module includes dependencies."""

from fastapi import Header, status, HTTPException

from constants import ID_KEY
from session import DATABASE_SESSION
from settings import INTERNAL_CONFIGS
from exceptions import TokenError
from repositories.auth import AuthRepository


async def verify_auth(
    x_auth: str = Header(description="Authorization token or API key"),
    x_from_name: str = Header(
        description="Name of services from where request is came", default=None
    ),
):
    """Check if user is logged in."""
    if x_from_name:
        api_config = INTERNAL_CONFIGS.get(x_from_name)
        if not api_config:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="X-From-Name header is invalid"
            )

        if api_config["api_key"] != x_auth:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="X-Auth token is invalid"
            )
    else:
        try:
            response = await AuthRepository.decode_token(x_auth)
            return response[ID_KEY]
        except TokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="X-Auth token is invalid"
            )


def get_database_session():
    """Get database session as dependency."""
    session = DATABASE_SESSION()
    try:
        yield session
    finally:
        session.close()
