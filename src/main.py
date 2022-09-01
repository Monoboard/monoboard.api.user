"""This module includes project entrypoint."""

from fastapi import FastAPI

from api.internal import router as internal_router
from api.user import router as user_router

app = FastAPI(title="monoboard-api-user")

app.include_router(internal_router)
app.include_router(user_router, prefix="/api/v1", tags=["user"])

