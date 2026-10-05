# Quotes API

A FastAPI service that serves programming quotes, with per-API-key rate limiting
backed by Redis. See `docs/architecture.md` for how the code is laid out.

## Run with Docker

```bash
make up      # start api + redis (http://localhost:8000)
make test    # run the test suite
make logs
make down
```

```bash
curl -i -H "X-API-Key: abc" localhost:8000/quote
```

Your local files are mounted into the container, so edits apply immediately.
Interactive API docs: http://localhost:8000/docs

## Expose a public URL

```bash
make tunnel   # prints a public https URL (Cloudflare quick tunnel, no account needed)
```

## Endpoints

All need an `X-API-Key` header and share one limit of 5 requests/minute per key:
`/quote`, `/quotes`, `/quotes/search?q=`, `/quotes/random`, `/quotes/{id}`,
`/authors`, `/authors/{id}/quotes`, `/tags`. `/health` is not limited.
