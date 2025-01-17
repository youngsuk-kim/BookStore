from pydantic import BaseModel, Field


class CreateBookResponseDTO(BaseModel):
    title: str = Field(..., description="Title")
    description: str = Field(..., description="Description")

