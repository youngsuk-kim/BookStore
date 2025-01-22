from enum import Enum

from sqlalchemy import String, Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.book.domain.enum.rental import RentalStatus
from core.db import Base
from core.db.mixins import TimestampMixin

class Rental(Base, TimestampMixin):
    """
    book 1-* rental *-1 user
    """

    __tablename__ = "rental"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: str = Column(String(255), nullable=False)
    user_id: Mapped[int] = Column(
		Integer,
        ForeignKey("user.id", ondelete="SET NULL", onupdate="CASCADE")
    )
    book_id: Mapped[int] = Column(
		Integer,
        ForeignKey("book.id", ondelete="SET NULL", onupdate="CASCADE")
    )
    rental_status = Column(Enum(RentalStatus), nullable=False)

    user = relationship("User", back_populates="rentals")
    book = relationship("Book", back_populates="rentals")

    @staticmethod
    def create(user, book, description):
        return Rental(
            user_id=user.id,
            book_id=book.id,
            description=description,
            rental_status=RentalStatus.REQUESTED
        )

    @property
    def rental_info(self) -> dict:
        """대여 정보 요약"""
        return {
            "rental_id": self.id,
            "description": self.description,
            "rental_status": self.rental_status.value,
            "user": self.user.name if self.user else None,
            "book": self.book.title if self.book else None
        }