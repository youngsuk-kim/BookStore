from sqlalchemy import select, and_

from app.book.domain.entity import Rental
from app.book.domain.entity.book import Book
from app.book.domain.repository.BookRepo import BookRepo
from core.db.session import session, session_factory


class BookSQLAlchemyRepo(BookRepo):
    async def save_rental(self, *, rental: Rental) -> None:
        session.add(rental)


    async def get_by_id(self, *, book_id: int) -> Book | None:
        async with session_factory() as read_session:
            stmt = await read_session.execute(
                select(Book).where(and_(Book.id == book_id))
            )
            return stmt.scalars().first()

    async def get_book_by_title_and_author(self, *, title: str, author: str) -> Book | None:
        async with session_factory() as read_session:
            stmt = await read_session.execute(
                select(Book).where(and_(Book.title == title, Book.author == author))
            )
            return stmt.scalars().first()

    async def create(self, *, book: Book) -> None:
        session.add(book)

