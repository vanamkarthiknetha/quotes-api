from fastapi import APIRouter, Depends, Query

from app.core.exceptions import NotFound
from app.core.feature_flags import is_enabled
from app.db.session import Database, get_db
from app.schemas.quote import QuoteOut
from app.services.quote_service import QuoteService
from app.services.search_service import SearchService

router = APIRouter(tags=["quotes"])


def service(db: Database = Depends(get_db)) -> QuoteService:
    return QuoteService(db)


@router.get("/quote", response_model=QuoteOut)
async def featured_quote(svc: QuoteService = Depends(service)):
    return svc.featured()


@router.get("/quotes", response_model=list[QuoteOut])
async def list_quotes(tag: str | None = None, svc: QuoteService = Depends(service)):
    return svc.list_all(tag)


@router.get("/quotes/random", response_model=QuoteOut)
async def random_quote(svc: QuoteService = Depends(service)):
    return svc.random()


@router.get("/quotes/search", response_model=list[QuoteOut])
async def search_quotes(
    q: str = Query(min_length=2, max_length=100),
    limit: int = Query(default=10, ge=1, le=50),
    db: Database = Depends(get_db),
):
    if not is_enabled("search_v2"):
        raise NotFound("Endpoint")
    return SearchService(db).search(q, limit)


@router.get("/quotes/{quote_id}", response_model=QuoteOut)
async def get_quote(quote_id: int, svc: QuoteService = Depends(service)):
    return svc.get(quote_id)
