from abc import ABC, abstractmethod

from app.book.domain.command import CreateBookCommand
from app.book.domain.entity.book import Book
from app.book.domain.usecase.book import BookUseCase
from core.db import session


class BookRepo(ABC):
    @abstractmethod
    async def create(self, book: Book) -> Book:
        return session.add(book)


class BookRepositoryAdapter:

    def __init__(self, *, book_repo: BookRepo):
        self.book_repo = book_repo

    async def create(self, book: Book) -> Book:
        return await self.book_repo.create(book)


class BookService(BookUseCase):
    def __init__(self, *, repository: BookRepositoryAdapter):
        self.repository = repository

    async def create_book(self, command: CreateBookCommand) -> Book:
        return await self.repository.create(Book(description=command.description))
