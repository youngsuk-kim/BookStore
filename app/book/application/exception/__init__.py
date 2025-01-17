from core.exceptions import CustomException


class BookDuplicatException(CustomException):
    code = 400
    error_code = "BOOK_DUPLICATE"
    message = "book already exists"