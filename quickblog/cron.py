
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

	# run every 300 seconds (5 minutes)
	run_every = 3
		
	def job(self):
		# This will be executed every 5 minutes
		sourcelink.test()

print '--cronScheduler.register is start.'
cronScheduler.register(CheckNews)