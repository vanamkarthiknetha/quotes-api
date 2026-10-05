from fastapi import APIRouter

from app import __version__
from app.schemas.common import HealthOut

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthOut)
async def health():
    return {"status": "ok", "version": __version__}
