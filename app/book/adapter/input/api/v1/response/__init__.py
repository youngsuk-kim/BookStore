from pydantic import BaseModel, Field


class CreateBookResponseDTO(BaseModel):
    title: str = Field(..., description="Title")
    description: str = Field(..., description="Description")

class CreateRentalResponseDTO(BaseModel):
    user_id: int = Field(..., description="User id")
    book_id: int = Field(..., description="Book id")
