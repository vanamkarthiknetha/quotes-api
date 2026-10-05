from app.core.exceptions import NotFound
from app.db.session import Database
from app.models import Author, Quote


class AuthorService:
    def __init__(self, db: Database):
        self.db = db

    def list_all(self) -> list[Author]:
        return self.db.authors.all()

    def quotes(self, author_id: int) -> list[Quote]:
        if self.db.authors.get(author_id) is None:
            raise NotFound("Author")
        return self.db.quotes.by_author(author_id)
