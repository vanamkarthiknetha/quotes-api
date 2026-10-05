from dataclasses import dataclass

from app.models.base import BaseModel


@dataclass
class Author(BaseModel):
    name: str
    born: int | None = None
    bio: str = ""
