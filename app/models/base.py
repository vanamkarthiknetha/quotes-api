from dataclasses import dataclass, field
from datetime import datetime, timezone


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class BaseModel:
    id: int
    created_at: datetime = field(default_factory=utcnow, kw_only=True)
