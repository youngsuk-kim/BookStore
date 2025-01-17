from pydantic import BaseModel


class CreateBookCommand(BaseModel):
    title: str
    author: str
    description: str

class CreateRentalCommand(BaseModel):
    book_id: int
    user_id: int
    description: str