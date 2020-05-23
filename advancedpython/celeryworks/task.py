#celery -A task worker --pool=solo --loglevel=info
import time
from celery import Celery

from advancedpython.celeryworks import my_app

app = Celery('task',
             backend='redis://0.0.0.0:6379',
             broker= "redis://0.0.0.0:6379")

@app.task()
def task():
    '''
    this is Asyncio task
    :return None:
    '''
    print("started task and sleep for 4 secs")
    time.sleep(4)
    print("completed")

