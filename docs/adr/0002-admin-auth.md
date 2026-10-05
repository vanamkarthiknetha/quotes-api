# ADR 0002: Admin endpoints need real auth

**Status:** proposed

`app/views/admin.py` exists but is not mounted. It must not be exposed until
admin users authenticate with something stronger than an API key.
