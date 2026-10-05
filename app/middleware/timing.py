import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.constants import PROCESS_TIME_HEADER


class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        response.headers[PROCESS_TIME_HEADER] = f"{(time.perf_counter() - start) * 1000:.1f}ms"
        return response
