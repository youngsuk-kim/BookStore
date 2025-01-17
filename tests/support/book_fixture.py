from app.book.domain.entity import Book


def make_book(
    id: int = 1,
    title: str = "test title",
    author: str = "test author",
    description: str = "test description",
):
    return Book(
        id=id,
        title=title,
        author=author,
        description=description,
    )
