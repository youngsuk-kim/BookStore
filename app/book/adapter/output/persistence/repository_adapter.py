
from app.book.domain.entity.book import Book
from app.book.domain.repository.BookRepo import BookRepo


class BookRepositoryAdapter:

    def __init__(self, *, book_repo: BookRepo):
        self.book_repo = book_repo

    async def create(self, *, book: Book) -> None:
        await self.book_repo.create(book=book)

    async def get_book_by_title_and_author(self, *, title: str, author: str) -> Book | None:
        return await self.book_repo.get_book_by_title_and_author(title=title, author=author)