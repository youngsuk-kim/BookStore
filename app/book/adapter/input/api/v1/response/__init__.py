from pydantic import BaseModel, Field


class BookResponse(BaseModel):
    id: int = Field(alias="id")
    title: str = Field(alias="title")
    author: str = Field(alias="author")
