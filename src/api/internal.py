"""This module includes api endpoints for internal usage."""

from http import HTTPStatus

from fastapi import APIRouter, Request
from fastapi.exceptions import RequestValidationError

from schemas.base import ResponseSchema
from utils.response import make_response


router = APIRouter()


@router.get(
    "/health",
    response_model=ResponseSchema,
    status_code=HTTPStatus.OK,
)
def health():
    """Respond with status OK for a health check."""
    return make_response(success=True, message=HTTPStatus.OK.phrase, http_status=HTTPStatus.OK)


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


def handle_validation_error(request: Request, exc: RequestValidationError):
    """Handle validation errors occurred during request.."""
    return make_response(
        success=False,
        message=HTTPStatus.UNPROCESSABLE_ENTITY.phrase,
        http_status=HTTPStatus.UNPROCESSABLE_ENTITY,
        data=exc.errors(),
    )
