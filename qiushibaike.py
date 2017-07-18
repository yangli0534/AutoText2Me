
                     # -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import thread
import time
import random
#糗事百科爬虫类
class qiushibaike:

    #初始化方法，定义一些变量
    def __init__(self):
        #self.pageIndex = 30
        #user_agent 从火狐 HttpFox中headers查找到
        #self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0)'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
        self.pageStories = []
        
    #传入某一页的索引获得页面代码
    def getPage(self):
        try:
            pageIndex = random.randint(2,35)
            url = 'https://www.qiushibaike.com/text/page/' + str(pageIndex)+'/'
            #构建请求的request
            request = urllib2.Request(url,headers = self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败,错误原因",e.reason
                return None


    #传入某一页代码，返回本页不带图片的段子列表
    def getPageItems(self):
        pageCode = self.getPage()
        if not pageCode:
            print "页面加载失败...."
            return None
        pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
        items = re.findall(pattern,pageCode)
        #print len(items)
        #print "*****items"
        #用来存储每页的段子们
        self.pageStories = []
        #遍历正则表达式匹配的信息
        i = 0
        for item in items:
            #如果不含有图片，把它加入list中
            #if not haveImg:
                replaceBR = re.compile('<.?span>')
                #将<br/> 用 换行符\n 替换
                text = re.sub(replaceBR,"\n",item[1])
                #item[0]是一个段子的发布者，item[1]是内容，item[2]是发布时间,item[4]是点赞数
                self.pageStories.append([item[0],text,item[2]])

                #strip()作用：去掉转义字符后输出
        #print item[0] +"-------0t"
        #print item[1] +"-------0T"
        #print text + "******TEXT"
        #print item[2] +"-------0t"
       
        #return pageStories

    #加载并提取页面的内容，加入到列表中
    def loadPage(self):
        #如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                #获取新一页
                #pageStories = self.getPageItems()
                self.getPageItems()
                #将该页的段子存放到全局list中
                if self.pageStories:
                    self.stories.append(self.pageStories)
                    #获取完之后页码索引加一，表示下次读取下一页
                    #self.pageIndex += 1

                #print len(self.stories)
    #调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self):
        #遍历一页的段子

        # for story in pageStories:
        #     #等待用户输入
        #     input = raw_input()
        #     #每当输入回车一次，判断一下是否要加载新页面
        #     self.loadPage()
        #     #如果输入Q则程序结束
        #     if input == "Q":
        #         self.enable = False
        #         return
        #     #print "$$$"
        #     print len(story)
        #     #现在网页已没有发布时间了
        #     #print u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" %(page,story[0],story[2],story[3],story[1])
        #     print u"第%d页\t发布人:%s\t赞:%s\n%s" %(page,story[0],story[2],story[1])
        self.loadPage()
        len_page = len(self.pageStories)
        story = self.pageStories[random.randint(0, len_page-1)]
        print u'回车看下一个，Q退出'
        input = raw_input()
        #     #每当输入回车一次，判断一下是否要加载新页面
        #     self.loadPage()
        #     #如果输入Q则程序结束
        if input == "Q":
            self.enable = False
            return
        #print len(story)
        print u'%s' %story[1]
    #开始方法
    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        #使变量为True，程序可以正常运行
        self.enable = True
       
        #先加载一页内容
        self.loadPage()
        
        #局部变量，控制当前读到了第几页
        #nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                #print len(self.stories)
                #print "-------stories"
                #从全局list中获取一页的段子
                self.pageStories = self.stories[0]
                #当前读到的页数加一
                #nowPage += 1
                #将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                #print "---------------------------------"
                #print len(pageStories)
                #print nowPage
                #输出该页的段子
                self.getOneStory()
    def getAJoke(self):
        self.enable = True
        self.loadPage()
        self.pageStories = self.stories[0]
        del self.stories[0]
        len_page = len(self.pageStories)
        story = self.pageStories[random.randint(0, len_page-1)]
        self.enable = True
        return story[1]

        #print u'回车看下一个，Q退出'
        #input = raw_input()
        #     #每当输入回车一次，判断一下是否要加载新页面
        #     self.loadPage()
        #     #如果输入Q则程序结束
        #if input == "Q":
        #   self.enable = False
        #    return
        #print len(story)
        #print u'%s' %story[1]

spider = qiushibaike()
spider.start()
#print spider.getAJoke()