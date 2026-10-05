from fastapi import Depends, Response

from app.core.clock import clock
from app.core.config import settings
from app.core.constants import (
    RATE_LIMIT_LIMIT_HEADER,
    RATE_LIMIT_REMAINING_HEADER,
    RATE_LIMIT_RESET_HEADER,
)
from app.core.exceptions import RateLimitExceeded
from app.core.security import get_api_key
from app.ratelimit.keys import build_key
from app.ratelimit.policies import DEFAULT_POLICY
from app.ratelimit.store import store


async def rate_limit(response: Response, api_key: str = Depends(get_api_key)) -> None:
    if not settings.rate_limit_enabled:
        return

    policy = DEFAULT_POLICY
    window_id = clock.window_id(policy.window_seconds)
    key = build_key(api_key, window_id)
    reset_in = clock.seconds_until_next_window(policy.window_seconds)

    count = await store.get(key)
    if count >= policy.limit:
        raise RateLimitExceeded(limit=policy.limit, retry_after=reset_in)

    await store.set(key, count + 1)

    response.headers[RATE_LIMIT_LIMIT_HEADER] = str(policy.limit)
    response.headers[RATE_LIMIT_REMAINING_HEADER] = str(policy.limit - count - 1)
    response.headers[RATE_LIMIT_RESET_HEADER] = str(reset_in)
