# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url,headers = headers)
    response  = urllib2.urlopen(request)
   # print response.read()

    ######_match_ string

    content = response.read().decode('utf-8')
    pattern = re.compile(r'<div.*?author clearfix".*?<img.*?<h2>(.*?)</h2>.*?<div.*?'+
                         'content">.*?<span>(.*?)</span>.*?<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print("auther:%s"%item[0])
        print("content:%s"%item[1])
        print("likes:%s\n"%item[2])

except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reaon'):
        print e.reason
