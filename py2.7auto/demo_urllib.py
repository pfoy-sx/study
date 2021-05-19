import urllib,urllib2
import re
#coding:utf8

def getHtml(url):
    page = urllib2.urlopen(url)
    return page.read()

def getImage(html):
    re_img = re.compile(r'<img class="BDE_Image" src="(.*?)".*?>')  ##匹配该页面的jpg文件
    img_list = re_img.findall(html)
    i = 0
    for imgurl in img_list:
        urllib.urlretrieve(imgurl,filename="%s.jpg" %i)    ##urlretrieve方法把url对应的文件下载到脚本当前目录下，可选参数filename指定下载文件名命名
        i += 1

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/4229162765'
    page = getHtml(url)
    getImage(page)