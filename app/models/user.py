from dataclasses import dataclass

from app.models.base import BaseModel


@dataclass
class User(BaseModel):
    email: str
    plan: str = "free"
    is_active: bool = True
