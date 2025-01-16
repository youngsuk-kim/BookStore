from sqlalchemy import String, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base
from core.db.mixins import TimestampMixin


class Rental(Base, TimestampMixin):
    """
    book 1-* rental *-1 user
    """

    __tablename__ = "rental"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: str = Column(String(255), nullable=False)
    user_id: Mapped[int] = mapped_column()
    book_id: Mapped[int] = mapped_column()
    user = relationship("User", back_populates="rentals")
    book = relationship("Book", back_populates="rentals")

