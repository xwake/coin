"""
Django settings for quickblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vp-5#1!1k8b9adr@(d^tmom*ca4$^6bba0u_3%ps3*y5u-3*$2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

#import djcelery
#djcelery.setup_loader()

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'djcelery',
    'celerytest',
    #'djangotasks',
    #'lambda',
    'kombu.transport.django',
    'django_cron',
    'proxy_cron',
    'checknews_cron',
)

#BROKER_URL = 'django://'
#CELERY_IMPORTS=("celerytest.tasks","quickblog.tasks","quickblog.task3")
#CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

#celery 
#BROKER_URL = 'django://'
#CELERY_ACCEPT_CONTENT = ['json']
#CELERY_RESULT_BACKEND='db+sqlite:///results.sqlite'
'''celerytest.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)'''
#DJANGOTASK_DAEMON_THREAD = True



'''
from datetime import timedelta
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celerytest.tasks.add',
        'schedule': timedelta(seconds=3),
        'args': (16, 16)
    },
}
CELERY_APP="quickblog.celeryInst"
CELERY_APP="celeryInst"

CELERY_IMPORTS=("celerytest.tasks",)
CELERY_IMPORTS=("tasks",)


print '--ok--',dir(djcelery)
print '--ok--',djcelery.__doc__
'''

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'quickblog.urls'

WSGI_APPLICATION = 'quickblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'blog.db.sqlite3'),
        'OPTIONS': {
        'timeout': 20,
    }
    }

}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'cn'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'



