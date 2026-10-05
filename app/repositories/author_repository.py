from app.models import Author
from app.repositories.base import InMemoryRepository


class AuthorRepository(InMemoryRepository[Author]):
    def by_name(self, name: str) -> Author | None:
        return next((a for a in self.all() if a.name.lower() == name.lower()), None)
