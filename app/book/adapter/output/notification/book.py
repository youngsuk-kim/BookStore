from abc import ABC, abstractmethod

class CreateBookNotification(ABC):
    @abstractmethod
    def notify(self, book_title: str):
        """책 생성 알림"""