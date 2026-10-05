from dataclasses import dataclass

from app.core.config import settings


@dataclass(frozen=True)
class RateLimitPolicy:
    name: str
    limit: int
    window_seconds: int


DEFAULT_POLICY = RateLimitPolicy(
    name="default",
    limit=settings.rate_limit_requests,
    window_seconds=settings.rate_limit_window_seconds,
)

PREMIUM_POLICY = RateLimitPolicy(name="premium", limit=100, window_seconds=60)
