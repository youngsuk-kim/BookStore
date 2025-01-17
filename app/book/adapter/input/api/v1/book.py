from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.book.adapter.input.api.v1.request import CreateBookRequest
from app.book.adapter.input.api.v1.response import CreateBookResponseDTO
from app.book.adapter.output.notification.book import CreateBookNotification
from app.book.domain.command import CreateBookCommand
from app.book.domain.usecase.book import BookUseCase
from app.container import Container

book_router = APIRouter()


@book_router.post(
    "",
    response_model=CreateBookResponseDTO,
)
@inject
async def create_book(
        request: CreateBookRequest,
        usecase: BookUseCase = Depends(Provide[Container.book_service]),
        notification: CreateBookNotification = Depends(Provide[Container.book_notification]),
):
    command = CreateBookCommand(**request.model_dump())
    await usecase.create_book(command=command)
    notification.notify(request.title)
    return {"title": request.title, "description": request.description}
