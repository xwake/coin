

from datetime import timedelta
import datetime
from celery import beat
from celeryInst import app as celery_app
from celery import Celery
import sys

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'quickblog.celeryInst.debug_task',
        'schedule': timedelta(seconds=5),
        'args': ()
    },
}

CELERY_TIMEZONE = 'UTC+8'

#app = Celery('quickblog')
#sch = beat.Scheduler(celery_app,schedule=CELERYBEAT_SCHEDULE)
#s = beat.Service(celery_app,scheduler_cls=sch)
#print dir(s)
#s.start()

#print '-- scheduler is created. ', datetime.datetime.now() ,__name__