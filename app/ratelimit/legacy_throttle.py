import time

from app.core.constants import LEGACY_RATE_LIMIT_PER_MINUTE


class TokenBucket:
    def __init__(self, rate_per_minute: int = LEGACY_RATE_LIMIT_PER_MINUTE):
        self.capacity = rate_per_minute
        self.tokens = float(rate_per_minute)
        self.refill_per_second = rate_per_minute / 60
        self.updated = time.monotonic()

    def allow(self) -> bool:
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.updated) * self.refill_per_second)
        self.updated = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False


_buckets: dict[str, TokenBucket] = {}


def allow(client_id: str) -> bool:
    return _buckets.setdefault(client_id, TokenBucket()).allow()
