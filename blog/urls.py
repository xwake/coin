from django.conf.urls import *
from blog.views import archive
from blog.views import celery
from blog.views import urlresult
from blog.models import TestTask
urlpatterns = patterns('', 
    url(r'^$',archive),
    url(r'^celery',celery),
    url(r'^urls',urlresult),
    #url(r'^test',testtask),
)



import django_cron,threading
django_cron.autodiscover()
#print '--django_cron is start.'

from django_cron import cronScheduler
#cronScheduler.execute()

t = threading.Thread(target = cronScheduler.execute(), args = ())
t.start()
t.join(10)
#print '--blog.urls.py > join finish'