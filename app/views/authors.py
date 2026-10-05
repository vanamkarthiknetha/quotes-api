from fastapi import APIRouter, Depends

from app.db.session import Database, get_db
from app.schemas.author import AuthorOut
from app.schemas.quote import QuoteOut
from app.services.author_service import AuthorService

router = APIRouter(prefix="/authors", tags=["authors"])


def service(db: Database = Depends(get_db)) -> AuthorService:
    return AuthorService(db)


@router.get("", response_model=list[AuthorOut])
async def list_authors(svc: AuthorService = Depends(service)):
    return svc.list_all()


@router.get("/{author_id}/quotes", response_model=list[QuoteOut])
async def author_quotes(author_id: int, svc: AuthorService = Depends(service)):
    return svc.quotes(author_id)
