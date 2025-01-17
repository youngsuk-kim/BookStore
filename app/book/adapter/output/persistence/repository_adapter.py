from app.book.domain.entity import Rental
from app.book.domain.entity.book import Book
from app.book.domain.repository.BookRepo import BookRepo


class BookRepositoryAdapter:

    def __init__(self, *, book_repo: BookRepo):
        self.book_repo = book_repo

    async def create(self, *, book: Book) -> None:
        await self.book_repo.create(book=book)

    async def get_book_by_title_and_author(self, *, title: str, author: str) -> Book | None:
        return await self.book_repo.get_book_by_title_and_author(title=title, author=author)

    async def get_book_by_id(self, *, book_id: int) -> Book | None:
        return await self.book_repo.get_by_id(book_id=book_id)

    async def save_rental(self, *, rental: Rental) -> None:
        return await self.book_repo.save_rental(rental=rental)