from app.core.config import settings


def build_key(api_key: str, window_id: int) -> str:
    return f"{settings.rate_limit_key_prefix}:{api_key}:{window_id}"


def parse_key(key: str) -> tuple[str, int]:
    _, api_key, window_id = key.rsplit(":", 2)
    return api_key, int(window_id)
