from app.models import Quote
from app.repositories.base import InMemoryRepository


class QuoteRepository(InMemoryRepository[Quote]):
    def by_author(self, author_id: int) -> list[Quote]:
        return [q for q in self.all() if q.author_id == author_id]

    def by_tag(self, tag: str) -> list[Quote]:
        return [q for q in self.all() if tag in q.tags]
