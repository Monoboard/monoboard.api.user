"""This module includes api endpoints for internal usage."""

from http import HTTPStatus

from fastapi import APIRouter

from utils.response import make_response


router = APIRouter()


@router.get("/health")
def health():
    """Respond with status OK for a health check."""
    return make_response(
        success=True,
        message=HTTPStatus.OK.phrase,
        http_status=HTTPStatus.OK
    )


def handle_404(*args):
    """Handle 404 not found error."""
    return make_response(
        success=False,
        message=HTTPStatus.NOT_FOUND.phrase,
        http_status=HTTPStatus.NOT_FOUND,
    )


def handle_405(*args):
    """Handle 405 method not allowed error."""
    return make_response(
        success=False,
        message=HTTPStatus.METHOD_NOT_ALLOWED.phrase,
        http_status=HTTPStatus.NOT_FOUND,
    )
