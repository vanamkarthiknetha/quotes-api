import os
from dataclasses import dataclass, field


def _bool(name: str, default: bool) -> bool:
    return os.getenv(name, str(default)).lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    app_name: str = "Quotes API"
    environment: str = field(default_factory=lambda: os.getenv("APP_ENV", "development"))
    debug: bool = field(default_factory=lambda: _bool("DEBUG", False))

    rate_limit_enabled: bool = field(default_factory=lambda: _bool("RATE_LIMIT_ENABLED", True))
    rate_limit_requests: int = field(default_factory=lambda: int(os.getenv("RATE_LIMIT_REQUESTS", "5")))
    rate_limit_window_seconds: int = field(default_factory=lambda: int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "60")))
    rate_limit_key_prefix: str = "rl"

    trusted_proxies: tuple[str, ...] = ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16")

    cache_ttl_seconds: int = field(default_factory=lambda: int(os.getenv("CACHE_TTL_SECONDS", "30")))

    slack_webhook_url: str | None = field(default_factory=lambda: os.getenv("SLACK_WEBHOOK_URL"))
    sentry_dsn: str | None = field(default_factory=lambda: os.getenv("SENTRY_DSN"))
    billing_endpoint: str | None = field(default_factory=lambda: os.getenv("BILLING_ENDPOINT"))


settings = Settings()
