from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base
from core.db.mixins import TimestampMixin


class Book(Base, TimestampMixin):
    """
    book *----1 user
    """

    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


