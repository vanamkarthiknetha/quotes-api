from pydantic import BaseModel, ConfigDict


class QuoteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    author_id: int
    text: str
    tags: list[str]
    likes: int = 0
