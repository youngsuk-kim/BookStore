from fastapi import APIRouter
from .v1.book import book_router as book_v1_router

router = APIRouter()
router.include_router(book_v1_router, prefix="/api/v1/book", tags=["Book"])


__all__ = ["router"]
