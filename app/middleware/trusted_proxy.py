import ipaddress

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings

_NETWORKS = [ipaddress.ip_network(n) for n in settings.trusted_proxies]


def _is_trusted(host: str | None) -> bool:
    try:
        return host is not None and any(ipaddress.ip_address(host) in n for n in _NETWORKS)
    except ValueError:
        return False


class TrustedProxyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        peer = request.client.host if request.client else None
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded and _is_trusted(peer):
            request.state.client_ip = forwarded.split(",")[0].strip()
        else:
            request.state.client_ip = peer
        return await call_next(request)
