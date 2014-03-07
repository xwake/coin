
import sys
sys.path.append("../")
from django_cron import cronScheduler, Job

# This is a function I wrote to check a feedback email address
# and add it to our database. Replace with your own imports
#from MyMailFunctions import check_feedback_mailbox
from blog import sourcelink

class CheckNews(Job):
    """
    Cron Job that checks the lgr users mailbox and adds any 
    approved senders' attachments to the db
    """

    # print '--class.checknews()'
    # run every 60 seconds (1 minutes)
    # run_every = 60*0.05 
    run_every = 60*0.1
        
    def job(self):
        # This will be executed every 5 minutes
        print '--class.checknews.job()'
        #sourcelink.test()
        sourcelink.dispatcher()
        #sourcelink.test()

#print '--cronScheduler.register is start.'
#cronScheduler.register(CheckNews)


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
