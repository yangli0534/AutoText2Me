##-*-coding: utf-8-*
#!/usr/bin/python
'''
Author : Leon
EMAIL: yangli0534@yahoo.com
Description: run a task on schedule

'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import schedule
import datetime
# Import smtplib for the actual sending function
#import smtplib

# Import the email modules we'll need
#from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open(textfile, 'rb')
# Create a text/plain message
t = datetime.datetime.now()
#    print "It's ",
#fp.read()mport time
f = open("MySchedule.py",'rb')
text = f.read()
f.close()
#msg = MIMEText( t.strftime("%A, %d. %B %Y %I:%M%p"))
#fp.close()

# me == the sender's email address
# you == the recipient's email address
#msg['Subject'] =  t.strftime("%A, %d. %B %Y %I:%M%p")#'The contents of '# % textfile
#
#import smtplib
 
toaddr = "yangli0534@yahoo.com"
password = "gomdocpagqgecbag"
fromaddr = "502327976@qq.com"
#server = smtplib.SMTP('smtp.yahoo.com', 587, None, 30)
#server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
server = smtplib.SMTP_SSL("smtp.qq.com", 465)
#server.ehlo()
#server.starttls()
#server.ehlo
server.login(fromaddr,password)
 
#msg = "YOUR MESSAGE:"+ t.strftime("%A, %d. %B %Y %I:%M%p")

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"+t.strftime("%A, %d. %B %Y %I:%M%p")

try: 
    body = "YOUR MESSAGE HERE"
    msg.attach(MIMEText(text, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print "send email successfully"
except:
    print "failed!"

    
