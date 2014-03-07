from django.conf.urls import *
from celerytest.views import celery

urlpatterns = patterns('', 
    url(r'^celery',celery),
    #url(r'^test',testtask),
)


