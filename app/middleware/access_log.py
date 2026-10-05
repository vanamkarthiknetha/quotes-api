import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.services import analytics_service

log = logging.getLogger("access")


def _timestamp() -> str:
    now = time.time()
    return time.strftime("%H:%M:%S", time.localtime(now)) + f".{int((now % 1) * 1000):03d}"


class AccessLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)

        path = request.url.path
        if request.url.query:
            path = f"{path}?{request.url.query}"

        api_key = request.headers.get("x-api-key", "-")
        forwarded = request.headers.get("x-forwarded-for")
        xff = forwarded.split(",")[0].strip() if forwarded else (getattr(request.state, "client_ip", None) or "-")

        analytics_service.record(api_key, request.url.path)
        log.info(f"{_timestamp()}  {request.method} {path:<28} {response.status_code}  xff={xff}  key={api_key}")
        return response
