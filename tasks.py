from celery import Celery
import time

celery = Celery('tasks',
                broker='redis://localhost:6379',
                backend='redis://localhost:6379')

@celery.task()
def stress_cpu():

    # stress the cpu
    for i in range(100000000):
        i = i + 1

    result = {
        "stress"  : "we have stressed the cpu"
    }
    return result