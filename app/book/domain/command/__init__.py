from pydantic import BaseModel


class CreateBookCommand(BaseModel):
    title: str
    author: str
