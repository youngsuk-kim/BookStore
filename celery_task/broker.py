from app.book.adapter.output.notification.book import CreateBookNotification
from celery_task.process import process_notification


class CreateNotification(CreateBookNotification):
    def notify(self, book_title: str):
        process_notification.delay(f"created book title: {book_title}")

