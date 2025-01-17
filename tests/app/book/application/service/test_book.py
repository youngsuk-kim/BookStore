from unittest.mock import AsyncMock

import pytest

from app.book.adapter.output.persistence.repository_adapter import BookRepositoryAdapter
from app.book.application.service.book import BookService
from app.book.domain.command import CreateBookCommand
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
from tests.support.user_fixture import make_user

repository_mock = AsyncMock(spec=BookRepositoryAdapter)
book_service = BookService(repository=repository_mock)

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