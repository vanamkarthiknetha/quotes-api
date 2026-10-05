import asyncio

from app.core.clock import clock
from app.core.config import settings
from app.ratelimit.keys import parse_key
from app.ratelimit.store import store


async def cleanup_once() -> int:
    current = clock.window_id(settings.rate_limit_window_seconds)
    removed = 0
    for key in await store.keys(prefix=f"{settings.rate_limit_key_prefix}:"):
        _, window_id = parse_key(key)
        if window_id < current:
            await store.delete(key)
            removed += 1
    return removed


async def run_forever(interval: int = 300) -> None:
    while True:
        await cleanup_once()
        await asyncio.sleep(interval)
