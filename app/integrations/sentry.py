import logging

from app.core.config import settings

log = logging.getLogger(__name__)


def init_sentry() -> None:
    if not settings.sentry_dsn:
        log.info("Sentry DSN not set, error reporting disabled")
        return
    log.info("Sentry would be initialised here for env=%s", settings.environment)
