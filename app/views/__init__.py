from fastapi import APIRouter, Depends

from app.ratelimit import rate_limit
from app.views import authors, health, home, quotes, tags

api_router = APIRouter(dependencies=[Depends(rate_limit)])
api_router.include_router(quotes.router)
api_router.include_router(authors.router)
api_router.include_router(tags.router)

public_router = APIRouter()
public_router.include_router(home.router)
public_router.include_router(health.router)
