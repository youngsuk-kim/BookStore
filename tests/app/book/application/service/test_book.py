from unittest.mock import AsyncMock

import pytest

from app.book.adapter.output.persistence.repository_adapter import BookRepositoryAdapter
from app.book.application.service.book import BookService
from app.book.domain.command import CreateBookCommand, CreateRentalCommand
from app.book.domain.entity import Book
from app.user.adapter.output.persistence.repository_adapter import UserRepositoryAdapter
from app.user.application.exception import (
    DuplicateEmailOrNicknameException,
    PasswordDoesNotMatchException,
    UserNotFoundException,
)
from app.user.application.service.user import UserService
from app.user.domain.command import CreateUserCommand
from app.user.domain.entity.user import UserRead
from core.helpers.token import TokenHelper
from tests.support.book_fixture import make_book
from tests.support.user_fixture import make_user

repository_mock = AsyncMock(spec=BookRepositoryAdapter)
user_repository_mock = AsyncMock(spec=UserRepositoryAdapter)
book_service = BookService(repository=repository_mock, user_repository=user_repository_mock)

@pytest.mark.asyncio
async def test_create_book():
    # Given
    command = CreateBookCommand(
        title="테스트 책 이름",
        author="테스트 저자 이름",
        description="테스트 책 설명 ~~~~~~~"
    )

    repository_mock.create.return_value = None
    repository_mock.get_book_by_title_and_author.return_value = None
    book_service.repository = repository_mock

    # When
    await book_service.create_book(command=command)

    # Then
    repository_mock.create.assert_awaited_once()

@pytest.mark.asyncio
async def test_create_rental():
    # Given
    test_book = make_book()
    test_user = make_user()

    repository_mock.save_rental.return_value = None
    repository_mock.get_book_by_id.return_value = test_book
    user_repository_mock.get_user_by_id.return_value = test_user
    book_service.repository = repository_mock
    book_service.user_repository = user_repository_mock

    command = CreateRentalCommand(book_id=test_book.id, user_id=test_user.id, description="test-description")

    # When
    await book_service.create_rental(command=command)

    # Then
    repository_mock.save_rental.assert_awaited_once()