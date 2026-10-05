from fastapi import FastAPI

from app.middleware.access_log import AccessLogMiddleware
from app.middleware.request_id import RequestIdMiddleware
from app.middleware.timing import TimingMiddleware
from app.middleware.trusted_proxy import TrustedProxyMiddleware


def register_middleware(app: FastAPI) -> None:
    app.add_middleware(AccessLogMiddleware)
    app.add_middleware(TimingMiddleware)
    app.add_middleware(TrustedProxyMiddleware)
    app.add_middleware(RequestIdMiddleware)
