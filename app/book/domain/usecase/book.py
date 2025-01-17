from abc import ABC, abstractmethod

from app.book.domain.command import CreateBookCommand, CreateRentalCommand


class BookUseCase(ABC):
    @abstractmethod
    async def create_book(self, command: CreateBookCommand) -> None:
        """create a new book"""

    @abstractmethod
    async def create_rental(self, command: CreateRentalCommand) -> None:
        """create a new rental"""
