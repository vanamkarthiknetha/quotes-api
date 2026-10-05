from dataclasses import dataclass

from app.models.base import BaseModel


@dataclass
class ApiKey(BaseModel):
    user_id: int
    key_hash: str
    label: str = "default"
    revoked: bool = False
