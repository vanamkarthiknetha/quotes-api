from dataclasses import dataclass

from app.models.base import BaseModel


@dataclass
class UsageRecord(BaseModel):
    api_key: str
    path: str
    status_code: int
