"""This module includes dependencies."""

from fastapi import Header, status, HTTPException

from session import DATABASE_SESSION
from settings import INTERNAL_API_KEYS


def verify_auth(
    x_auth: str = Header(description="Authorization token or API key"),
    x_from_name: str = Header(
        description="Name of services from where request is came", default=None
    ),
):
    """Check if user is logged in."""
    if x_from_name:
        api_key = INTERNAL_API_KEYS.get(x_from_name)
        if not api_key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="X-From-Name header is invalid"
            )

        if api_key != x_auth:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="X-Auth header is invalid"
            )


def get_database_session():
    """Get database session as dependency."""
    session = DATABASE_SESSION()
    try:
        yield session
    finally:
        session.close()
