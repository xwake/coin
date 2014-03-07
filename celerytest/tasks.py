from __future__ import absolute_import
from celery import shared_task
from celery import Celery

#app = Celery('tasks',backend='db+sqlite:///results.sqlite',  broker='django://')
app = Celery('tasks',broker='django://')
'''
app.conf.CELERY_TASK_SERIALIZER = 'json'
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Oslo',
    CELERY_ENABLE_UTC=True,
)
'''
print '--celerytest.tasks is created.'

@app.task
def add(x, y):
    print '--celerytest.tasks.add() is run.'
    return x + y