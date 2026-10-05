from app.core.constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE


def clamp_page(offset: int = 0, limit: int = DEFAULT_PAGE_SIZE) -> tuple[int, int]:
    return max(offset, 0), min(max(limit, 1), MAX_PAGE_SIZE)


def paginate(items: list, offset: int, limit: int) -> dict:
    offset, limit = clamp_page(offset, limit)
    return {"items": items[offset : offset + limit], "total": len(items), "offset": offset, "limit": limit}
