# coding:utf-8
import re
import urllib2
from bs4 import BeautifulSoup


#获取起始网页源码
def gethtml(url):
    request = urllib2.Request(url)
    html = urllib2.urlopen(request)
    gothtml = html.read()
    return gothtml

#获取待爬网址列表
def get_urllist(allurl):
    urllist = []
    for eachurl in allurl:
        eachurl = 'http://opinion.people.com.cn' + eachurl
        urllist.append(eachurl)
    urllist.pop(0)#删除第一个不匹配项
    return urllist

#保存文章
def save_passage(urllist):
    for one in urllist:
        s2 = gethtml(one)
        passage = re.findall('id="p_content\" class="clearfix">(.*?)<span id="paper_num">',s2,re.S)
        time = re.findall('<span id="paper_num">(.*?)</span></p>',s2)
        title = re.findall('<title>(.*?)</title>',s2,re.S)[0]

        for i in passage:
            f = open('/Users/ss/Documents/people/demo/%s.doc' % title,'w')
            f.writelines(title)
            f.writelines(time)
            f.writelines(i+ '\n')
        f.close()


print '--------------Star-------------'
url = 'http://opinion.people.com.cn/GB/8213/49160/49217/index.html'
html = gethtml(url)
allurl = re.findall('<a href=\'(.*?)\' class=\"abl"',html, re.S)
urllist = get_urllist(allurl)
save_passage(urllist)
print '--------------End--------------'