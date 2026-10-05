from dataclasses import dataclass, field

from app.models.base import BaseModel


@dataclass
class Quote(BaseModel):
    author_id: int
    text: str
    tags: list[str] = field(default_factory=list)
    likes: int = 0
