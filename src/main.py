"""This module includes project entrypoint."""

from fastapi import FastAPI

from api.user import router as user_router

app = FastAPI(title="monoboard-api-user")

app.include_router(
    user_router,
    prefix="/api/v1",
    tags=["user"],
)

