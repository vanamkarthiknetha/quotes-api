import asyncio

import httpx
import pytest

from app.main import app
from app.ratelimit import LIMIT

HEADERS = {"X-API-Key": "test-key"}
ENDPOINTS = ["/quote", "/quotes", "/quotes/search?q=code", "/quotes/random", "/quotes/1", "/authors", "/authors/1/quotes", "/tags"]


async def _fire(path: str, n: int) -> list[int]:
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        return [(await client.get(path, headers=HEADERS)).status_code for _ in range(n)]


@pytest.mark.parametrize("path", ENDPOINTS)
def test_requests_over_limit_are_rejected(path):
    codes = asyncio.run(_fire(path, LIMIT + 3))
    assert codes.count(200) == LIMIT
    assert codes.count(429) == 3


def test_limit_is_shared_across_endpoints():
    async def run():
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            return [(await client.get(p, headers=HEADERS)).status_code for p in ENDPOINTS]

    assert asyncio.run(run()).count(200) == LIMIT


def test_api_key_is_case_insensitive(get):
    codes = [get("/quote", {"X-API-Key": k}).status_code for k in ["Abc", "ABC", "abc", " abc", "aBc", "abc "]]
    assert codes.count(200) == LIMIT


def test_429_has_retry_after(get):
    for _ in range(LIMIT):
        get("/quote")
    response = get("/quote")
    assert response.status_code == 429
    assert int(response.headers["Retry-After"]) > 0
