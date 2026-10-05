import asyncio
import os

import redis.asyncio as aioredis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
LATENCY = float(os.getenv("STORE_LATENCY_MS", "15")) / 1000


class CounterStore:
    async def get(self, key: str) -> int:
        await asyncio.sleep(LATENCY)
        async with aioredis.from_url(REDIS_URL, decode_responses=True) as client:
            value = await client.get(key)
            return int(value) if value is not None else 0

    async def set(self, key: str, value: int) -> None:
        await asyncio.sleep(LATENCY)
        async with aioredis.from_url(REDIS_URL, decode_responses=True) as client:
            await client.set(key, value)

    async def delete(self, key: str) -> None:
        async with aioredis.from_url(REDIS_URL, decode_responses=True) as client:
            await client.delete(key)

    async def keys(self, prefix: str = "") -> list[str]:
        async with aioredis.from_url(REDIS_URL, decode_responses=True) as client:
            return await client.keys(f"{prefix}*")

    def clear(self) -> None:
        import redis

        client = redis.from_url(REDIS_URL)
        client.flushdb()
        client.close()


store = CounterStore()
