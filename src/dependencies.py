"""This module includes dependencies."""

from fastapi import Header, status, HTTPException


async def verify_token(x_token: str = Header()):
    """Check if user is logged in."""
    # TODO: access token or api key
    if not x_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-Token header invalid"
        )
