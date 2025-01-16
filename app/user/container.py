from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton

from app.book.adapter.output.persistence.sqlalchemy.book import BookSQLAlchemyRepo
from app.book.application.service.book import BookRepositoryAdapter
from app.user.adapter.output.persistence.repository_adapter import UserRepositoryAdapter
from app.user.adapter.output.persistence.sqlalchemy.user import UserSQLAlchemyRepo
from app.user.application.service.user import UserService


class UserContainer(DeclarativeContainer):
    wiring_config = WiringConfiguration(modules=["app"])

    user_sqlalchemy_repo = Singleton(UserSQLAlchemyRepo)
    user_repository_adapter = Factory(
        UserRepositoryAdapter,
        repository=user_sqlalchemy_repo,
    )
    user_service = Factory(UserService, repository=user_repository_adapter)

    book_sqlalchemy_repo = Singleton(UserSQLAlchemyRepo)
    book_repository_adapter = Factory(
        BookRepositoryAdapter,
        repository=book_sqlalchemy_repo,
    )
    book_service = Factory(UserService, repository=book_repository_adapter)