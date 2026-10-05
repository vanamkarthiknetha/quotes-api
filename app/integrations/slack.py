import logging

import httpx

from app.core.config import settings

log = logging.getLogger(__name__)


async def notify(text: str) -> None:
    if not settings.slack_webhook_url:
        log.debug("slack disabled, would have sent: %s", text)
        return
    async with httpx.AsyncClient(timeout=5) as client:
        await client.post(settings.slack_webhook_url, json={"text": text})
