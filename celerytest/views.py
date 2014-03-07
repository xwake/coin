from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
# Create your views here.


def celery(request):
    #import sys
    #sys.path.append("../celerytest")
    #print sys.path
    #from tasks import add
    #r = add.delay(3,5) 
    #print add(3,5)
    #print '--r1:',r 
    #print '--r.ready:',r.ready()
    #print '--r.id:',r.id
    i = 0
    flag = 10
    '''
    while r.ready()==False and i < flag:
        print '--r:',r.ready() 
        i = i + 1
        
    try:
        #print r.get(timeout=1)
        print r.get(propagate=False)
        print r.traceback
    except:
        pass
'''
    t = loader.get_template("archive.html")
    c = Context({'posts':'abc'})

    return HttpResponse(t.render(c))


