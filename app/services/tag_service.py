from collections import Counter

from app.core.config import settings
from app.core.feature_flags import is_enabled
from app.db.session import Database
from app.services.cache import TTLCache

_cache = TTLCache(settings.cache_ttl_seconds)


class TagService:
    def __init__(self, db: Database):
        self.db = db

    def counts(self) -> list[dict]:
        if is_enabled("response_cache") and (cached := _cache.get("tags")) is not None:
            return cached
        counter = Counter(t for q in self.db.quotes.all() for t in q.tags)
        result = [{"name": name, "count": n} for name, n in sorted(counter.items())]
        _cache.set("tags", result)
        return result
