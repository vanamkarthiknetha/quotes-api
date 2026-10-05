from fastapi import Header

from app.core.exceptions import Unauthorized


def normalize_api_key(raw: str) -> str:
    return raw.strip().lower()


async def get_api_key(x_api_key: str | None = Header(default=None)) -> str:
    if not x_api_key or not x_api_key.strip():
        raise Unauthorized()
    return normalize_api_key(x_api_key)
