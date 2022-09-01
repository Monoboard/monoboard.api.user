"""This module provides helper functionality for web responses."""

from fastapi.responses import JSONResponse


def make_response(success: bool, http_status, subcode=None, data=None, message=None):
    """Return formatted json response."""
    response = {
        "success": success,
        "message": message,
        "subcode": subcode,
        "data": data
    }
    return JSONResponse(response, status_code=http_status)
