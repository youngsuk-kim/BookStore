from pydantic import BaseModel, Field


class CreateBookRequest(BaseModel):
    title: str = Field(..., description="Title")
    author: str = Field(..., description="Author")
