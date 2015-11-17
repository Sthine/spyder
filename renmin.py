# coding:utf-8
import os
import getpass
import re
import urllib2


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
def save_passage(urllist, user_path):
    for one in urllist:
        s2 = gethtml(one)
        passage = re.findall('id="p_content\" class="clearfix">(.*?)<span id="paper_num">',s2,re.S)
        time = re.findall('<span id="paper_num">(.*?)</span></p>',s2)
        title = re.findall('<title>(.*?)</title>',s2,re.S)[0]

        for i in passage:
            f = open(user_path + '/%s.doc' % title, 'w')
            f.writelines(title)
            f.writelines(time)
            f.writelines(i + '\n')
        f.close()


print '--------------Star-------------\n说明：''' \
      '下载的文件默认保存在桌面名为重要言论库的文件夹\n'\
      '---------------------------------------'

user_input = raw_input('请输入要下载的文章类型的序号，1.评论员  2.社论\n')
if user_input == '1':
    url = 'http://opinion.people.com.cn/GB/8213/49160/49217/index.html'
    user_select = 'pinglunyuan'
elif user_input == '2':
    url = 'http://opinion.people.com.cn/GB/8213/49160/49179/index.html'
    user_select = 'shelun'

print '下载开始'
user_name = getpass.getuser()
user_path = 'C:/users/'+ user_name +'/desktop/' + user_select
os.makedirs(user_path)
html = gethtml(url)
allurl = re.findall('<a href=\'(.*?)\' class=\"abl"',html, re.S)
urllist = get_urllist(allurl)
save_passage(urllist, user_path)
print '下载结束\n--------------End--------------'
