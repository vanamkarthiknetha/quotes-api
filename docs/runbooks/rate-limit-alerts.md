# Runbook: rate limit alerts

**Alert:** `HighRequestRatePerKey` fires when one key exceeds 3x its limit.

1. Find the key in the access logs.
2. Check whether traffic comes through the load balancer (X-Forwarded-For).
3. Check `RATE_LIMIT_ENABLED` is not set to false in the environment.
4. If the key is abusive, revoke it with `scripts/generate_api_key.py` and rotate.
