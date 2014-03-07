


from __future__ import absolute_import
from hyz import apihelper

'''
print '----------------------------------'
apihelper.info(django_cron)
print '----------------------------------'
apihelper.info(django_cron.autodiscover())
'''

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
#from .celery_scheduler import CELERYBEAT_SCHEDULE as cs
#from .celeryInst import app as celery_app


'''
from celery.task.base import periodic_task
from django.utils.timezone import timedelta

print '----init---'
@periodic_task(run_every=timedelta(seconds=2))
def my_background_process():
    # insert code
    print '----somethin---'


    '''


