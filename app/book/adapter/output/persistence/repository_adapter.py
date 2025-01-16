from app.book.domain.entity.book import Book
from app.book.domain.repository.BookRepo import BookRepo


class BookRepositoryAdapter:

    def __init__(self, *, book_repo: BookRepo):
        self.book_repo = book_repo

    async def create(self, book: Book) -> Book:
        return await self.book_repo.create(book)
