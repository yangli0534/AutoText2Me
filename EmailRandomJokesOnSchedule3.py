# -*- coding:gb2312 -*-

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
import urllib2
import re
import schedule
import time
import datetime

class randomJoke:

    #初始化方法
    def __init__(self):
        self.url = 'http://lengxiaohua.com/random'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #笑话内容
        self.content = []

    #获取网页源代码
    def getSourceCode(self):
        try:
            request = urllib2.Request(url = self.url, headers=self.headers)
            response = urllib2.urlopen(request)
            sourceCode = response.read().decode('utf-8')
            return sourceCode
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"网络错误...",e.reason
                return None

    #获取笑话
    def setContent(self):
        sourceCode = self.getSourceCode()
        if not sourceCode:
            print('获取网页内容失败~！')
            quit()
        pattern = re.compile(' <pre.*?js="joke_summary".*?"first_char">(.*?)</span>(.*?)</pre>.*?class="user_info">.*?<a.*?>(.*?)</a>.*?(.*?)',re.S)
        items = re.findall(pattern,sourceCode)
        self.content = items
        #print u"已经爬取源代码...正在解析源代码..."

    #返回笑话
    def getContent(self):
        return self.content

    #打印一则笑话
    def printAJoke(self,number):
        joke = self.content[number]
        print u"作者:%s" %(joke[2])
        print u'发表于:'+ joke[3]
        #item[0]和item[1]组成完整的内容
        print joke[0]+joke[1]

    def getAJoke(self,number):
        joke = self.content[number]
        content = ""
        #content = content+ u"作者:" %(joke[2])
        #print u'发表于:'+ joke[3]
        #item[0]和item[1]组成完整的内容
        content =  joke[0]+joke[1]
        return content

def job():
    global myRandomJoke
    #global server
    global toaddr
    global fromaddr
    global password
    t = datetime.datetime.now()
    content = ""
    content = content+ u"你好，这里是随机笑话！"
    content = content+ "It's "
    content = content+ t.strftime("%A, %d. %B %Y %I:%M%p")+'\n'
    myRandomJoke.setContent()
    #myRandomJoke.printAJoke(2)
    content = content + myRandomJoke.getAJoke(2)
    print content
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Leon send a joke for u on"+t.strftime("%A, %d. %B %Y %I:%M%p")
    
    try:
        body = "YOUR MESSAGE HERE"
        #msg.attach(MIMEText(content, 'plain'))
        #msg.attach(MIMEText(content, 'plain'))
        msg.attach(MIMEText(content,format,'utf-8'))
        text = msg.as_string()
        #server = smtplib.SMTP_SSL("smtp.126.com", 25)# connect to email server
        server = smtplib.SMTP("smtp.139.com",25)# connect to email server
        server.login(fromaddr,password)
        #server.sendmail(fromaddr, toaddr, text)
        server.sendmail(fromaddr, toaddr2, text)
        server.sendmail(fromaddr, fromaddr,text)
        server.quit()
        print "send email successfully"
    except:
        print "failed!"

toaddr = "xxxxxxx" # email address to send
toaddr2 = "xxxxxx"
fromaddr = "xxxxxxxx"
password = "xxxxxxxxx"
#server = smtplib.SMTP('smtp.yahoo.com', 587, None, 30)
#server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
#server = smtplib.SMTP_SSL("smtp.qq.com", 465)# connect to email server

#server = smtplib.SMTP_SSL("smtp.qq.com", 465)# connect to email server
#server.login(fromaddr,password)
myRandomJoke = randomJoke()
job()
schedule.every(10).minutes.do(job)
#notQuit = True
#print u"你好，这里是随机笑话！"
while True:
    schedule.run_pending()
    time.sleep(10)
    


server.quit()
quit()
