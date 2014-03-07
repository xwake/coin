from __future__ import absolute_import

from datetime import timedelta
from celery import Celery
app = Celery('quickblog',
              broker='django://',
              #backend='db+sqlite:///blog.db.sqlite3',
              include=['quickblog.task5'])
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERYBEAT_SCHEDULE = {
        "add": {
                "task": "quickblog.task5.add",
                "schedule": timedelta(seconds=3),
                "args": (13, 14)
                }, },
                )
if __name__ == '__main__':
    app.start()