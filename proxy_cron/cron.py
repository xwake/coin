# coding=gbk
#encoding = utf-8

import sys
sys.path.append("../")
sys.path.append("../blog/proxy")
from django_cron import cronScheduler, Job

# This is a function I wrote to check a feedback email address
# and add it to our database. Replace with your own imports
#from MyMailFunctions import check_feedback_mailbox
import proxyUpdate as proxy
debug = 0

class ProxyUpdate(Job):
    """
    Cron Job that checks the lgr users mailbox and adds any 
    approved senders' attachments to the db
    """

    # print '--class.checknews()'
    # run every 60 seconds (1 minutes)
    # run_every = 60*0.05 
    run_every = 60*60*24    #每天检查一次
    #run_every=60*0.1
        
    def job(self):
        # This will be executed every 5 minutes
        if debug: print '--class.ProxyUpdate.job()'
        #sourcelink.test()
        proxy.main()
        #sourcelink.test()

#print '--cronScheduler.register is start.'
cronScheduler.register(ProxyUpdate)
#cronScheduler.execute()


'''
from dateutil.tz import tzlocal
localtimezone = tzlocal.get_localzone()
print '--localtimezone:',localtimezone
'''

#import time
#print '--',time.timezone
#print '--','Etc/GMT%+d' % (time.timezone / 3600)
#offsetHour = time.timezone / 3600
#return 'Etc/GMT%+d' % offsetHour
