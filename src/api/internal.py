"""This module includes api endpoints for internal usage."""

from fastapi import APIRouter, status


router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
def health():
    """Respond with status OK for a health check."""
    return {"status": True}
