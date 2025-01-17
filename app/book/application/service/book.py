
from app.book.adapter.output.persistence.repository_adapter import BookRepositoryAdapter
from app.book.application.exception import BookDuplicatException
from app.book.domain.command import CreateBookCommand, CreateRentalCommand
from app.book.domain.entity import Rental
from app.book.domain.entity.book import Book
from app.book.domain.usecase.book import BookUseCase
from app.user.adapter.output.persistence.repository_adapter import UserRepositoryAdapter
from core.db import Transactional


class BookService(BookUseCase):
    def __init__(self, *, repository: BookRepositoryAdapter, user_repository: UserRepositoryAdapter):
        self.repository = repository
        self.user_repository = user_repository

    @Transactional()
    async def create_rental(self, command: CreateRentalCommand) -> None:
        found_user = await self.user_repository.get_user_by_id(user_id=command.user_id)
        found_book = await self.repository.get_book_by_id(book_id=command.book_id)

        new_rental = Rental.create(found_user, found_book, command.description)

        await self.repository.save_rental(rental=new_rental)

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

