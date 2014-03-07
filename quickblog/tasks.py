from __future__ import absolute_import
from .celeryInst import app
import datetime
import celery

#app = Celery('tasks',backend='db+sqlite:///results.sqlite',  broker='django://')
#app = Celery('tasks',broker='django://')
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
#print '--app is created.'
print '--quickblog.tasks.add.task() '

@app.task
def add(x, y):
    print '---quickblog.tasks.add() is run'
    return x + y



@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=5))
def myfunc():
    print 'periodic_task'