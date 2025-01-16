from abc import ABC, abstractmethod

from app.book.adapter.output.persistence.repository_adapter import BookRepositoryAdapter
from app.book.domain.command import CreateBookCommand
from app.book.domain.entity.book import Book
from app.book.domain.usecase.book import BookUseCase
from core.db import session


class BookService(BookUseCase):
    def __init__(self, *, repository: BookRepositoryAdapter):
        self.repository = repository

    async def create_book(self, command: CreateBookCommand) -> Book:
        return await self.repository.create(Book(description=command.description))
