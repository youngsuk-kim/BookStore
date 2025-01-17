from abc import abstractmethod, ABC

from app.book.domain.entity.book import Book


class BookRepo(ABC):
    @abstractmethod
    async def create(self, *, book: Book) -> Book:
        """"create a new book"""

