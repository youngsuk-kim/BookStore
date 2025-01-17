from abc import abstractmethod, ABC

from app.book.domain.entity.book import Book


class BookRepo(ABC):
    @abstractmethod
    async def create(self, *, book: Book) -> Book:
        """"create a new book"""
    @abstractmethod
    async def get_book_by_title_and_author(self, *, title: str, author: str) -> Book | None:
        """get one book"""

