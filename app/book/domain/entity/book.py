from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base
from core.db.mixins import TimestampMixin

class Book(Base, TimestampMixin):
    """
    book *----1 user
    """

    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: str = Column(String(255), nullable=False)
    author: str = Column(String(255), nullable=False)
    description: str = Column(String(255), nullable=False)

    rentals = relationship('Rental', back_populates='book')

