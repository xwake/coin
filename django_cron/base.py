#coding=gbk
"""
Copyright (c) 2007-2008, Dj Gilcrease
All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import cPickle
from threading import Timer
from datetime import datetime
import pytz

from django.dispatch import dispatcher
from django.conf import settings

from signals import cron_done
import models

# how often to check if jobs are ready to be run (in seconds)
# in reality if you have a multithreaded server, it may get checked
# more often that this number suggests, so keep an eye on it...
# default value: 300 seconds == 5 min
polling_frequency = getattr(settings, "CRON_POLLING_FREQUENCY", 60*0.5)
debug = 1

class Job(object):
    # 86400 seconds == 24 hours
    run_every = 86400

    def run(self, *args, **kwargs):  
        self.job()
        cron_done.send(sender=self, *args, **kwargs)
        
    def job(self):
        """
        Should be overridden (this way is cleaner, but the old way - overriding run() - will still work)
        """
        pass

class CronScheduler(object):
    def register(self, job_class, *args, **kwargs):
        """
        Register the given Job with the scheduler class
        """
        
        job_instance = job_class()
        
        if not isinstance(job_instance, Job):
            raise TypeError("You can only register a Job not a %r" % job_class)

        job, created = models.Job.objects.get_or_create(name=str(job_instance.__class__))
        if created:
            job.instance = cPickle.dumps(job_instance)
        job.args = cPickle.dumps(args)
        job.kwargs = cPickle.dumps(kwargs)
        job.run_frequency = job_instance.run_every
        job.save()

    def execute(self):
        """
        Queue all Jobs for execution
        """
        #print '--base.py > execute() is running...'
        status, created = models.Cron.objects.get_or_create(pk=1)
        
        # This is important for 2 reasons:
        #     1. It keeps us for running more than one instance of the
        #        same job at a time
        #     2. It reduces the number of polling threads because they
        #        get killed off if they happen to check while another
        #        one is already executing a job (only occurs with
        #         multi-threaded servers)
        if debug and status.executing==True :print '--base.py > status.executing:',status.executing,datetime.now()
        if status.executing:
            #print '--base.py > status.executing is True, return >>'
            return

        status.executing = True
        try:
            status.save()
            pass
        except:
            # this will fail if you're debugging, so we want it
            # to fail silently and start the timer again so we 
            # can pick up where we left off once debugging is done
            Timer(polling_frequency, self.execute).start()
            print '--base.py > status.save() exception'
            return
            
        jobs = models.Job.objects.all()
        #if debug: print '--base.py > len.jobs', len(jobs)
        for job in jobs:
            
            if debug and job.queued == 0: print '--          job.queued:',job.queued
            if job.queued:

                # 此处的时间格式(offset-native & offset-aware)有极大影响，与settings.py的设置高度相关。

                #print '\ndatetime.now():',datetime.now()
                #print 'datetime.now(pytz.utc):',datetime.now(pytz.utc)
                #print 'job.last_run:',job.last_run
                #print dir(pytz.utc)

                #USE_TZ = True（两者都是offset-aware，带时区信息)
                #time_delta = datetime.now(pytz.utc) - job.last_run

                #USE_TZ = False（两者都是offset-native，不带时区信息)
                time_delta = datetime.now() - job.last_run
                #print '--time_delta:',(time_delta.seconds + 86400*time_delta.days) 
                #print '--', job.run_frequency
                if (time_delta.seconds + 86400*time_delta.days) > job.run_frequency:
                #if 1>0 :
                    if debug: print '\n--base.py > job start'
                    inst = cPickle.loads(str(job.instance))
                    args = cPickle.loads(str(job.args))
                    kwargs = cPickle.loads(str(job.kwargs))
                    
                    inst.run(*args, **kwargs)
                    job.last_run = datetime.now()
                    job.save()

                    '''
                    try:
                        inst.run(*args, **kwargs)
                        job.last_run = datetime.now()
                        job.save()
                        
                    except Exception,e:
                        # if the job throws an error, just remove it from
                        # the queue. That way we can find/fix the error and
                        # requeue the job manually
                        print dir(e)
                        print e.__doc__
                        print '--run error'
                        #job.queued = False
                        job.save()
                        '''
                else:
                    if debug:
                        #print '--base.py > pass. time_delta:',(time_delta.seconds + 86400*time_delta.days) ,'/job.run_frequency:', job.run_frequency
                        pass


        status.executing = False
        status.save()
        
        # Set up for this function to run again
        Timer(polling_frequency, self.execute).start()


cronScheduler = CronScheduler()

