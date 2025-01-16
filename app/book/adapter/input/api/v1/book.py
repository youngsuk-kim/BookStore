from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.book.adapter.input.api.v1.request import CreateBookRequest
from app.container import Container
from app.user.application.dto import CreateUserResponseDTO
from app.user.domain.command import CreateUserCommand
from app.user.domain.usecase.user import UserUseCase

book_router = APIRouter()


@book_router.post(
    "",
    response_model=CreateUserResponseDTO,
)
@inject
async def create_user(
    request: CreateBookRequest,
    usecase: UserUseCase = Depends(Provide[Container.user_service]),
):
    command = CreateUserCommand(**request.model_dump())
    await usecase.create_user(command=command)
    return {"email": request.email, "nickname": request.nickname}


