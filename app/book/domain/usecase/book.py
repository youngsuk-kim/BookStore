from abc import ABC, abstractmethod

from app.book.domain.command import CreateBookCommand


class BookUseCase(ABC):
    @abstractmethod
    async def create_book(self, command: CreateBookCommand) -> None:
        """create a new book"""
