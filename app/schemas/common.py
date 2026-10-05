from pydantic import BaseModel


class ErrorOut(BaseModel):
    detail: str


class HealthOut(BaseModel):
    status: str
    version: str
