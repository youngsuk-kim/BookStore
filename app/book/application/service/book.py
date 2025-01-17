
from app.book.adapter.output.persistence.repository_adapter import BookRepositoryAdapter
from app.book.application.exception import BookDuplicatException
from app.book.domain.command import CreateBookCommand
from app.book.domain.entity.book import Book
from app.book.domain.usecase.book import BookUseCase
from core.db import Transactional


class BookService(BookUseCase):
    def __init__(self, *, repository: BookRepositoryAdapter):
        self.repository = repository

    @Transactional()
    async def create_book(self, command: CreateBookCommand) -> None:
        create_book = Book(
            title=command.title,
            author=command.author,
            description=command.description,
        )

        found_book = await self.repository.get_book_by_title_and_author(title=command.title, author=command.author)

        if found_book is not None:
            raise BookDuplicatException()

        await self.repository.create(book=create_book)

