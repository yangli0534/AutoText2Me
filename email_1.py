##-*-coding: utf-8-*
#!/usr/bin/python
'''
Author : Leon
EMAIL: yangli0534@yahoo.com
Description: run a task on schedule

'''


import schedule
import datetime
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
#from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open(textfile, 'rb')
# Create a text/plain message
t = datetime.datetime.now()
#    print "It's ",
#fp.read()mport time


#msg = MIMEText( t.strftime("%A, %d. %B %Y %I:%M%p"))
#fp.close()

# me == the sender's email address
# you == the recipient's email address
#msg['Subject'] =  t.strftime("%A, %d. %B %Y %I:%M%p")#'The contents of '# % textfile
#
#import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587, None, 30)
#server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
server.ehlo()
server.starttls()
server.ehlo
server.login("yangli0534@gmail.com","wd15210579762@")
 
msg = "YOUR MESSAGE:"+ t.strftime("%A, %d. %B %Y %I:%M%p")
server.sendmail("yangli0534@gmail.com", "yangli0534@yahoo.com", msg)
server.quit()
    

    
