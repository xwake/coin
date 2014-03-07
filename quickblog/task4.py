#coding=gbk


from celery import Celery

app = Celery('task4', broker='django://')

@app.task
def add4(x, y):
    return x + y