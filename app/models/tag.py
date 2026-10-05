from dataclasses import dataclass

from app.models.base import BaseModel


@dataclass
class Tag(BaseModel):
    name: str
    description: str = ""
