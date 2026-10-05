from fastapi import APIRouter

from app.ratelimit import store
from app.services import analytics_service

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/usage/{api_key}")
async def usage(api_key: str):
    return analytics_service.usage_for(api_key)


@router.post("/rate-limit/reset")
async def reset_rate_limits():
    store.clear()
    return {"ok": True}
