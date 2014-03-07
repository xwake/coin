from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
import datetime

from datetime import timedelta
from hyz import apihelper


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quickblog.settings')
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'quickblog.celeryInst.debug_task',
        'schedule': timedelta(seconds=30),
        'args': ()
    },
}

app = Celery('quickblog.tasks.add',
                broker='django://',
                schedule=CELERYBEAT_SCHEDULE,
                include=['quickblog.tasks'])



# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    print '-------debug_task()'



#print dir(app)
#app.run()
#apihelper.info(app)
if __name__ == '__main__':
    app.start()

#export DJANGO_SETTINGS_MODULE="settings"
#CELERYD_CHDIR="./quickblog"

#print ' celery.py is run, task is define.', datetime.datetime.now() ,__name__

'''
if __name__ == "__main__":
    print ' celery.py is run.', datetime.datetime.now() 
    #apihelper.info(app)'''