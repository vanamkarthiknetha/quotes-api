from fastapi import APIRouter, Depends

from app.db.session import Database, get_db
from app.schemas.tag import TagOut
from app.services.tag_service import TagService

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("", response_model=list[TagOut])
async def list_tags(db: Database = Depends(get_db)):
    return TagService(db).counts()
