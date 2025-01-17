from time import sleep

from celery_task import celery_app

processing_time = 5

@celery_app.task
def process_notification(a):
    print("Processing notification {}".format(a))
    sleep(processing_time)
    print("End processing notification {}".format(a))
    return a
