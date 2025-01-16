from app.book.domain.entity.book import Book
from app.book.domain.repository.BookRepo import BookRepo
from core.db.session import session


class BookSQLAlchemyRepo(BookRepo):
    async def create(self, book: Book) -> Book:
        return session.add(book)

