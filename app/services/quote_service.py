import random

from app.core.exceptions import NotFound
from app.db.session import Database
from app.models import Quote


class QuoteService:
    def __init__(self, db: Database):
        self.db = db

    def featured(self) -> Quote:
        return self.db.quotes.get(1)

    def list_all(self, tag: str | None = None) -> list[Quote]:
        return self.db.quotes.by_tag(tag) if tag else self.db.quotes.all()

    def random(self) -> Quote:
        return random.choice(self.db.quotes.all())

    def get(self, quote_id: int) -> Quote:
        quote = self.db.quotes.get(quote_id)
        if quote is None:
            raise NotFound("Quote")
        return quote
