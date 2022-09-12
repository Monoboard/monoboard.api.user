"""This module provides helper functionality for web responses."""

from fastapi import status
from fastapi.responses import JSONResponse


def make_response(
    success: bool,
    http_status: status,
    subcode: str = None,
    message: str = None,
    data: dict = None,
):
    """Return formatted json response."""
    response = {
        "success": success,
        "message": message,
        "subcode": subcode,
        "data": data,
    }
    return JSONResponse(response, status_code=http_status)
