"""This module includes project entrypoint."""

from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError

from api.internal import router as internal_router, handle_404, handle_405, handle_401, handle_validation_error
from api.user import router as user_router
from settings import APP_NAME

app = FastAPI(title=APP_NAME)

app.include_router(internal_router)
app.include_router(user_router, prefix="/api/v1", tags=["user"])

app.add_exception_handler(status.HTTP_401_UNAUTHORIZED, handle_401)
app.add_exception_handler(status.HTTP_404_NOT_FOUND, handle_404)
app.add_exception_handler(status.HTTP_405_METHOD_NOT_ALLOWED, handle_405)
app.add_exception_handler(RequestValidationError, handle_validation_error)
app.add_exception_handler(RequestValidationError, handle_validation_error)
