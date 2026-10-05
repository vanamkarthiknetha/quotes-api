import time
from typing import Any


class TTLCache:
    def __init__(self, ttl_seconds: int):
        self.ttl = ttl_seconds
        self._data: dict[str, tuple[float, Any]] = {}

    def get(self, key: str) -> Any | None:
        hit = self._data.get(key)
        if hit is None:
            return None
        expires_at, value = hit
        if time.monotonic() > expires_at:
            self._data.pop(key, None)
            return None
        return value

    def set(self, key: str, value: Any) -> None:
        self._data[key] = (time.monotonic() + self.ttl, value)

    def clear(self) -> None:
        self._data.clear()
