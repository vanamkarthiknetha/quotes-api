import logging

from app.core.config import settings
from app.core.feature_flags import is_enabled

log = logging.getLogger(__name__)


async def report_usage(api_key: str, units: int) -> None:
    if not is_enabled("usage_billing") or not settings.billing_endpoint:
        return
    log.info("billing: %s used %d units", api_key, units)
