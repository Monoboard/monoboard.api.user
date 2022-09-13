"""This module include functionality to work with auth microservice."""

from http import HTTPStatus

from repositories.base import BaseRepository
from constants import TOKEN_KEY
from settings import INTERNAL_CONFIGS
from exceptions import TokenError, APIError


class AuthRepository(BaseRepository):
    """Class that includes http requests to auth microservice."""

    api_name = "monoboard.api.auth"
    api_config = INTERNAL_CONFIGS[api_name]

    api_url = "http://{host}:{port}".format(
        host=api_config["api_host"], port=api_config["api_port"]
    )
    api_version = "v1"
    api_key = api_config["api_key"]

    @classmethod
    async def decode_token(cls, token: str):
        """Request auth microservice to decode token."""
        request_headers = cls.format_headers()
        request_url = cls.format_url("decode/")
        response, response_status = await cls.post(
            request_url, headers=request_headers, body={TOKEN_KEY: token}
        )
        if response_status != HTTPStatus.OK:
            raise TokenError(
                message=response.message,
                subcode=response.subcode,
            )

        return response.data
