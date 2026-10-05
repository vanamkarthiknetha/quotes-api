import asyncio
import uuid

import httpx
import pytest

from app.main import app
from app.ratelimit import store
from app.services import analytics_service


@pytest.fixture(autouse=True)
def clean_state():
    store.clear()
    analytics_service.reset()
    yield


@pytest.fixture
def api_key() -> str:
    return f"test-{uuid.uuid4()}"


@pytest.fixture
def get(api_key):
    def _get(path: str, headers: dict | None = None):
        async def run():
            transport = httpx.ASGITransport(app=app)
            async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
                return await client.get(path, headers={"X-API-Key": api_key} if headers is None else headers)

        return asyncio.run(run())

    return _get
