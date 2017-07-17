##-*-coding: utf-8-*
#!/usr/bin/python
'''
Author : Leon
EMAIL: yangli0534@yahoo.com
Description: run a task on schedule

'''


import schedule
import datetime
import time

def job():
    t = datetime.datetime.now()
    print "It's ",
    print   t.strftime("%A, %d. %B %Y %I:%M%p")
    return

schedule.every(1).minutes.do(job)
print "I am going to work"
while True:
    schedule.run_pending()
    time.sleep(10) # wait one minute
    

    

    
