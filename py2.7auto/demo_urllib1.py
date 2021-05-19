# #coding:utf8
# import urllib,urllib2
# import re,time,sys
#
# def getPage(page_num=1):
#     url = 'http://www.qiushibaike.com/8hr/page/' + str(page_num)
#     ua ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81 (Edition Baidu)'   ##浏览器信息
#     request = urllib2.Request(url,headers={'User-Agent':ua})     ##伪装浏览器并连接 url
#     response = urllib2.urlopen(request)
#     html = response.read()
#     return html
#
# def getPagecoent(page_num=1):
#     html = getPage(page_num)
#     ##re.s表示'.’可以匹配换行符，否则不匹配换行符
#     re_page = re.compile(r'<div class="author.*?>.*?<a.*?<img.*?alt="(.*?)"/>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>.*?<div class="stats">.*?<i class="number">(\d+)</i>',re.S)
#     ##匹配<br/>正则表达式
#     replaceBR = re.compile(r'<br/>')
#     items = re_page.findall(html)
#     page_contents = []
#     for item in items:
#         content = replaceBR.sub('\n',item[1].strip())
#         page_contents.append([page_num,item[0].strip(),item[2].strip(),content])
#     return page_contents
#
# def getOnestory(page_contents):
#     for story in page_contents:
#         input = raw_input()
#         if input.lower() == 'q':
#             sys.exit()
#         print "第%d页\t发布人：%s\t共%s赞\n内容：%s\n" %(story[0],story[1],story[2],story[3])
#         print '------------------------------------------------------------分隔符------------------------------------------------------------'
#     time.sleep(1)
#     return True
#
# if __name__ == '__main__':
#     print '回车继续，Q or q 退出！-----------------------------------------'
#     num = 20
#     while True:
#         page_contents = getPagecoent(num)
#         getOnestory(page_contents)
#         num +=1
#
