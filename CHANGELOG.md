# Changelog

## 2.5.0
- New `/quotes/search` endpoint (search_v2).
- Search results are cached for `CACHE_TTL_SECONDS`.

## 2.4.1
- Rate limit headers on successful responses.
- API keys are now case-insensitive.

## 2.4.0
- Added authors and tags endpoints.
- Response cache for tags.

## 2.0.0
- Reworked the rate limiter and moved counters to Redis.
