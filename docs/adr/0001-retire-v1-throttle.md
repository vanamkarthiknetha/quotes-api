# ADR 0001: Retire the v1 token bucket

**Status:** in progress

`app/ratelimit/legacy_throttle.py` is no longer used by any route.
Delete it once the v1 billing export is switched off.
