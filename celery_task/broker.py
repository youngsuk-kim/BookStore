from celery_task.process import process_notification


def create_notification(body: str):
    process_notification.delay(body)