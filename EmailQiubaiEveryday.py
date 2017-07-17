#-*- coding:utf-8 -*-


#!/usr/bin/python
__author__ = 'Leon'

'''
    Author : Leon
    Email  : yangli0534@yahoo.com
    Description: 1 grab a joke from the Internet 
                 2 email to someone on schedule 
                 3 参考了部分网友的代码 ，感谢。侵权删
'''
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import re
import schedule
import time
import datetime
from qiushibaike import qiushibaike

def job():
    #global myRandomJoke
    global myQiuBai
    #global server
    global toaddr
    global fromaddr
    global password
    t = datetime.datetime.now()
    content = ''
    content = content+ u'笑口常开！'
    content = content+ u"It's "
    content = content+ t.strftime("%A, %d. %B %Y %I:%M%p")+'\n'
    #myRandomJoke.setContent()
    #myRandomJoke.printAJoke(2)
    #content = content + myRandomJoke.getAJoke(2)
    content = content + myQiuBai.getAJoke()
    print content
    #content = u'''你好，这是一封测试邮件，来自yangli0534@yahooc.com'''
    #content = content +t.strftime("%A, %d. %B %Y %I:%M%p")
    msg = MIMEMultipart()
    msg['From'] =fromaddr
    msg['To'] =','.join(toaddr)
    msg['Cc'] = ','.join(ccaddr)
    msg['Bcc'] = ','.join(ccaddr)
    msg['Subject'] = u"Leon send a joke to you on"+t.strftime("%A, %d. %B %Y %I:%M%p")
    
    try:
        #body = "YOUR MESSAGE HERE"
        body = content
        #msg.attach(MIMEText(content, 'plain'))
        #msg.attach(MIMEText(content, 'plain'))
        #msg.attach(MIMEText(content,format,'utf-8'))
        msg.attach(MIMEText(body.encode('gbk')))
        text = msg.as_string()
        #server = smtplib.SMTP_SSL("smtp.126.com", 25)# connect to email server
        server = smtplib.SMTP("smtp.139.com",25)# connect to email server
        server.login(fromaddr,password)
        #server.sendmail(fromaddr, toaddr, text)
        server.sendmail(fromaddr, toaddr + ccaddr, text)
        #server.sendmail(fromaddr, fromaddr,text)
        server.quit()
        print "send email successfully"
    except:
        print "failed!"

toaddr = ['1184802734@qq.com','18811007706@139.com'] # email address to send
ccaddr = ['502327976@qq.com'] # carbon copy
bccaddr = ['15210579762@139.com']#blind carbon copy
#toaddr2 = '502327976@qq.com'
fromaddr = 'china__mobile@139.com'#send address
password = "xxxxxxxxx"#password
#server = smtplib.SMTP('smtp.yahoo.com', 587, None, 30)
#server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
#server = smtplib.SMTP_SSL("smtp.qq.com", 465)# connect to email server

#server = smtplib.SMTP_SSL("smtp.qq.com", 465)# connect to email server
#server.login(fromaddr,password)
#myRandomJoke = randomJoke()
myQiuBai = qiushibaike() # 
job()
schedule.every(1).minutes.do(job)# send a email every 2 minutes
#notQuit = True
#print u"你好，这里是随机笑话！"
while True:
    schedule.run_pending()# 
    time.sleep(10)
    


server.quit()
quit()
