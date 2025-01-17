
from app.book.adapter.output.persistence.repository_adapter import BookRepositoryAdapter
from app.book.domain.command import CreateBookCommand
from app.book.domain.entity.book import Book
from app.book.domain.usecase.book import BookUseCase
from core.db import session, Transactional


class BookService(BookUseCase):
    def __init__(self, *, repository: BookRepositoryAdapter):
        self.repository = repository

    @Transactional()
    async def create_book(self, command: CreateBookCommand) -> None:
        book = Book(
            title=command.title,
            author=command.author,
            description=command.description,
        )

        await self.repository.create(book=book)
