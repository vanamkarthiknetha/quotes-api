# INC-2048: Rate limit not enforced — one API key far exceeds its quota

| Field | Value |
|---|---|
| Priority | P1 |
| Status | Open |
| Component | Public API / rate limiting |
| Reported by | Customer Success, on behalf of Northwind Learning |
| Environment | Production, v2.5.0 |
| First seen | 2 days ago, shortly after the v2.5.0 release |

## Summary

Every API key is limited to **5 requests per minute**, shared across all quote,
author and tag endpoints. A single key belonging to Northwind Learning (free
plan) is receiving **30 to 50 successful responses per minute**. Infrastructure
cost attributed to this customer has roughly tripled.

## Impact

- One free-plan key is consuming paid-tier levels of traffic.
- The limit is the control that protects shared capacity; it is not holding.
- Likely affects any client that sends requests in bursts, not just this one.

## Customer report

> Our quote-of-the-day widget refreshes for every classroom when the school day
> starts, so our backend fires a batch of requests all at once from a few app
> servers. It mostly just works. We occasionally get a 429 but retrying clears
> it, so we never changed our plan. Some of our services send the key in upper
> case, some in lower case.

## What support has checked

- Single API key, `NWL-PROD-7731`, sometimes sent as `nwl-prod-7731`.
- Traffic is spread across `/quotes/search`, `/quotes/random`, `/tags` and the
  other quote endpoints. They all share the same 5/min limit.
- Requests arrive from several IPs through the customer's load balancer, so
  `X-Forwarded-For` changes between requests.
- `RATE_LIMIT_ENABLED=true` in production. Limit confirmed at 5 per 60 seconds.
- Other free-plan customers do receive 429s, so the limiter is not globally off.

## Steps to reproduce

1. Start the service: `make up`.
2. Pick one API key and one endpoint (any of the rate-limited routes).
3. Replay the customer's pattern: send a batch of requests for that key as fast
   as the client can issue them (their job fans out across app servers), then a
   few more requests spread over the rest of the same minute.
4. Count the `200` responses for that key within the minute. Far more than 5
   succeed. Watch it live with `make logs`.

## Log sample

Access log for the customer's key, one minute of production traffic:

```
08:00:00.412  GET /quotes/search?q=learning  200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:00.415  GET /quotes/search?q=learning  200  xff=203.0.113.22  key=nwl-prod-7731
08:00:00.418  GET /quotes/search?q=science   200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:00.421  GET /quotes/search?q=learning  200  xff=203.0.113.31  key=NWL-PROD-7731
08:00:00.423  GET /quotes/random             200  xff=203.0.113.22  key=nwl-prod-7731
08:00:00.426  GET /quotes/search?q=history   200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:00.430  GET /quotes/search?q=learning  200  xff=203.0.113.31  key=NWL-PROD-7731
08:00:00.433  GET /tags                      200  xff=203.0.113.22  key=NWL-PROD-7731
08:00:00.436  GET /quotes/search?q=learning  200  xff=203.0.113.22  key=NWL-PROD-7731
08:00:00.441  GET /quotes/random             200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:00.450  GET /quotes/search?q=math      200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:00.462  GET /tags                      200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:00.475  GET /quotes/search?q=learning  200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:00.489  GET /quotes/search?q=history   200  xff=203.0.113.14  key=nwl-prod-7731
08:00:00.500  GET /quotes/search?q=reading   200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:00.514  GET /quotes/search?q=reading   200  xff=203.0.113.14  key=NWL-PROD-7731
... 18 more 200s for this key between 08:00:00.5 and 08:00:00.9 ...
08:00:12.204  GET /quotes/search?q=math      200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:19.877  GET /quotes/random             200  xff=203.0.113.31  key=nwl-prod-7731
08:00:26.310  GET /quotes/search?q=art       200  xff=203.0.113.22  key=NWL-PROD-7731
08:00:33.645  GET /tags                      200  xff=203.0.113.14  key=NWL-PROD-7731
08:00:41.902  GET /quotes/search?q=math      429  xff=203.0.113.14  key=NWL-PROD-7731
08:00:41.950  GET /quotes/search?q=math      429  xff=203.0.113.31  key=nwl-prod-7731
```

Roughly 39 successful responses for one key in the 08:00 minute; the limit is 5.

## Expected

No API key receives more than 5 successful (`200`) responses per minute. Once
the limit is reached, further requests return `429` until the next minute,
regardless of endpoint, source IP or key casing.

## Acceptance criteria

- Root cause identified and fixed.
- The existing test suite still passes.
