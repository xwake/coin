#coding=gbk
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogPost
from blog.models import UrlResult

# Create your views here.
 
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))

def urlresult(request):
    urls = UrlResult.objects.all()
    t = loader.get_template("urls.html")
    c = Context({'urls':urls})
    return HttpResponse(t.render(c))




#print '\n----------------------------------------------views.py start---'
#f = getattr(TestTask(),'printSome')
#print 'TestTask().printSome.im_self.pk:',TestTask().printSome.im_self.pk

#djangotasks.register_task(TestTask.printSome, "dd") #valid
#print '\n------register done'


'''
#可运动，但方法内的内容好像没被调用
import djangotasks
from blog.models import TestTask
from hyz import apihelper
tp = TestTask().printSome
tp.im_self.pk = 1
djangotasks.register_task(tp, "dd")
task = djangotasks.task_for_object( tp )
djangotasks.run_task(task)
'''
#print '\n----------------------------------------------views.py end---'


def celery(request):
    import sys
    sys.path.append("../celerytest")
    print sys.path
    #from tasks import add
    #r = add.delay(3,5) 
    #r.wait()

    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})

    return HttpResponse(t.render(c))