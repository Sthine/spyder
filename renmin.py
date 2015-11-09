# coding:utf-8
import re
import urllib2

#获取起始网页源码
def gethtml(url):
    request = urllib2.Request(url)
    html = urllib2.urlopen(request)
    gothtml = html.read()
    return gothtml


url = 'http://opinion.people.com.cn/GB/8213/49160/49217/index.html'
shelun_url = 'http://opinion.people.com.cn/GB/8213/49160/49179/index1.html'
print('获取起始网页开始')
s = gethtml(shelun_url)
print('获取起始网页完成')

print('待爬网页装载开始')

urllist = []
allurl = re.findall('<a href=\'(.*?)\' class=\"abl"',s, re.S)
for eachurl in allurl:
    eachurl = 'http://opinion.people.com.cn' + eachurl
    urllist.append(eachurl)
urllist.pop(0)#删除第一个不匹配项

print(len(urllist))
print('所有待爬网页装载完成')

print('文章爬行开始')
passagelist = []
for aurl in urllist:
    s2 = gethtml(aurl)
    passage = re.findall('id="p_content\" class="clearfix">(.*?)<span id="paper_num">',s2,re.S)
    time = re.findall('<span id="paper_num">(.*?)</span></p>',s2)
    title = re.findall('<title>(.*?)</title>',s2,re.S)[0]

    for i in passage:
        f = open('/Users/ss/Documents/people/shelun/%s.doc' % title,'w')
        f.writelines(title)
        f.writelines(time)
        f.writelines(i+ '\n')
        f.close()
print('文章爬行结束')