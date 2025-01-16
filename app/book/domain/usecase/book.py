from abc import ABC, abstractmethod

from app.book.domain.command import CreateBookCommand
from app.book.domain.entity.book import Book


class BookUseCase(ABC):
    @abstractmethod
    async def create_book(self, command: CreateBookCommand) -> Book:
        """create a new book"""
