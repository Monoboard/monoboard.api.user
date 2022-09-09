"""This module includes dependencies."""

from fastapi import Header, status, HTTPException

from session import DATABASE_SESSION


def verify_token(x_token: str = Header()):
    """Check if user is logged in."""
    # TODO: access token or api key
    if not x_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-Token header invalid"
        )


def get_database_session():
    """Get database session as dependency."""
    session = DATABASE_SESSION()
    try:
        yield session
    finally:
        session.close()
