from __future__ import absolute_import
from celery.task.base import periodic_task
from django.utils.timezone import timedelta
from celery import Celery
'''
app = Celery('quickblog.tasks.add',
                broker='django://',
                schedule=CELERYBEAT_SCHEDULE,
                include=['quickblog.tasks'])
'''
app = Celery('quickblog',
                broker='django://',task='quickblog.task3')

print '----task3---'
@periodic_task(run_every=timedelta(seconds=2))
def kk():
    # insert code
    print '----somethin---'