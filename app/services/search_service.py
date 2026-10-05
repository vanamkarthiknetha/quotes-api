from app.core.config import settings
from app.core.feature_flags import is_enabled
from app.db.session import Database
from app.models import Quote
from app.services.cache import TTLCache
from app.utils.strings import tokenize

_cache = TTLCache(settings.cache_ttl_seconds)


class SearchService:
    def __init__(self, db: Database):
        self.db = db

    def search(self, query: str, limit: int = 10) -> list[Quote]:
        cache_key = f"{query.lower()}:{limit}"
        if is_enabled("response_cache") and (cached := _cache.get(cache_key)) is not None:
            return cached
        terms = set(tokenize(query))
        scored = [(len(terms & set(tokenize(q.text))), q) for q in self.db.quotes.all()]
        result = [q for score, q in sorted(scored, key=lambda s: -s[0]) if score][:limit]
        _cache.set(cache_key, result)
        return result
