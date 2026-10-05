# Architecture

```
request -> middleware (request id, proxy, timing, access log)
        -> views (FastAPI routers)
        -> rate limit dependency (app/ratelimit)
        -> services -> repositories -> in-memory db
```

- **views/** HTTP layer only. No business logic.
- **services/** business logic. One service per resource.
- **repositories/** data access. In-memory today, Postgres later (see `migrations/`).
- **ratelimit/** per-API-key rate limiting, backed by Redis.
- **middleware/** cross-cutting concerns.
- **workers/** background jobs run outside the API process.
