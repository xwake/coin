from __future__ import absolute_import

from quickblog.celeryStart import app


@app.task
def add(x, y):
    print '---someth.task5.add(%d,%d)'%(x,y)
    return x + y