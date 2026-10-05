from app.db import seed
from app.repositories.author_repository import AuthorRepository
from app.repositories.quote_repository import QuoteRepository


class Database:
    def __init__(self):
        self.quotes = QuoteRepository(seed.QUOTES)
        self.authors = AuthorRepository(seed.AUTHORS)


db = Database()


def get_db() -> Database:
    return db
