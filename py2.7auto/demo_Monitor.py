#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/26 15:58
# @Author  : Beam
# @Site    : 
# @File    : demo_Monitor.py
# @Software: PyCharm

import pycurl
import os,sys,time


def sendMail(errorlist):
    import smtplib
    import string
    txt = errorlist
    HOST = 'smtp.126.com'   ##定义SMTP主机
    SUBJECT = 'Interface Error!'   ##邮件主题
    TO = ['beam.l@xuehu365.com','506556658@qq.com']  ##收件地址
    FROM = 'a506556658@126.com'    ##发件地址
    BODY =string.join(("From: %s" %FROM,"To: %s" % TO, "Subject: %s" % SUBJECT,"",txt),"\r\n")     ##组装sendmail方法的邮件主题内容，每段内容以\r\n进行分隔
    try:
        server = smtplib.SMTP()   ##创建smtp()对象
        server.connect(HOST,25)   ##通过connenct方法链接smtp主机
        server.starttls()         ##启动安全传输模式
        server.login("a506556658@126.com","506556658@qq.com")    ##邮箱账号登录校验
        server.sendmail(FROM,TO,BODY)    ##邮件发送
        server.quit()    ##断开smtp链接
        return True
    except Exception,e:
        print "失败：" + str(e)
        return False

def getCode(URL):
#获取状态码,并返回url对应的状态码的字典
    list = []
    c = pycurl.Curl()
    c.setopt(pycurl.URL,URL) #定义请求的URL常量
    c.setopt(pycurl.CONNECTTIMEOUT,30) #请求等待时间最多5秒
    c.setopt(pycurl.TIMEOUT,30)   #定义请求超时时间（服务器没回应）
    c.setopt(pycurl.NOPROGRESS,1) #屏蔽下载进度条
    c.setopt(pycurl.FORBID_REUSE,1) #交互完成后强制断开连接，不重用
    c.setopt(pycurl.MAXREDIRS,1)  #指定HTTP重定向的最大数为1
    c.setopt(pycurl.DNS_CACHE_TIMEOUT,60) #设置DNS信息保存时间为30秒
    c.setopt(pycurl.USERAGENT,"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81 (Edition Baidu)")
    with open(os.path.dirname(os.path.realpath(__file__))+"/Monitmp.txt","wb") as indexfile:
        c.setopt(pycurl.WRITEHEADER,indexfile)   #将返回的HTTP HEADER定向到indexfile文件对象
        c.setopt(pycurl.WRITEDATA,indexfile)     #将返回的HTML内容定向到indexfile文件对象
        try:
            c.perform()
        except Exception,e:
            print "Connection error:" +str(e)
            c.close()
            sys.exit()
    code = c.getinfo(c.HTTP_CODE)
    #list = [URL,code]
    return code

def getdic(urls):
    dic = {}
    for j in range(0,4):
        if j == 0:
            for i in urls:
                code = getCode(i)
                #time.sleep(1)
                dic[i] = [code,0]
        else:
            for i in urls:
                code = getCode(i)
                #time.sleep(1)
                if int(code) == 200 or int(code) == 301 or int(code) == 302 or int(code) == 304:
                    dic[i][0] = code
                    dic[i][1] = 0
                else:
                    dic[i][0] = code
                    dic[i][1] = dic[i][1] + 1
        time.sleep(600)
    else:
        return dic

def main():
    dic = {}
    count = 0
    n = 0
    #接口
    urls = ['http://app.xuehu365.com/login', 'http://app.xuehu365.com/phone_msg', 'http://app.xuehu365.com/client/bind_mobile', 'http://app.xuehu365.com/client/personal_info_edit', 'http://app.xuehu365.com/client/wallet/amount', 'http://app.xuehu365.com/index', 'http://api.xuehu365.com/courses/my_order_list', 'http://app.xuehu365.com/version', 'http://app.xuehu365.com/room/enter', 'http://app.xuehu365.com/room/page', 'http://app.xuehu365.com/room/msg_sent', 'http://app.xuehu365.com/room/question_trans', 'http://app.xuehu365.com/room/live_answer', 'http://app.xuehu365.com/room/question_page', 'http://app.xuehu365.com/room/question_detail', 'http://app.xuehu365.com/room/question_answer', 'http://app.xuehu365.com/room/chat_page', 'http://app.xuehu365.com/intranet/msg_push', 'http://app.xuehu365.com/room/tips/pay', 'http://app.xuehu365.com/room/member/list', 'http://app.xuehu365.com/room/click', 'http://app.xuehu365.com/notify/list', 'http://app.xuehu365.com/intranet/notify/push_by_all', 'http://app.xuehu365.com/intranet/community/create', 'http://app.xuehu365.com/community/chat/enter', 'http://app.xuehu365.com/community/msg_sent', 'http://app.xuehu365.com/community/member/personal_details', 'http://api.xuehu365.com/intranet/order/to_buy', 'http://api.xuehu365.com/intranet/order/commit_order', 'http://api.xuehu365.com/intranet/order/buy', 'http://api.xuehu365.com/intranet/order/price_adjust', 'http://api.xuehu365.com/intranet/order/my_order_list', 'http://api.xuehu365.com/intranet/order/order_list', 'http://api.xuehu365.com/intranet/order/cancel', 'http://api.xuehu365.com/intranet/order/refund', 'http://api.xuehu365.com/intranet/apply/sign_up', 'http://api.xuehu365.com/intranet/apply/edit', 'http://api.xuehu365.com/intranet/manager/apply/audit', 'http://api.xuehu365.com/intranet/manager/apply/apply_cancel', 'http://api.xuehu365.com/intranet/user/recharge_wallet', 'http://api.xuehu365.com/user/gift', 'http://api.xuehu365.com/room/member/list', 'http://api.xuehu365.com/community/member/list', 'http://api.xuehu365.com/intranet/phone_msg', 'http://app.xuehu365.com/intranet/client/bind_mobile']
    dic = getdic(urls)
    for key in dic:
        if not int(dic[key][0]) == 200 or int(dic[key][0]) == 301 or int(dic[key][0]) == 302 or int(dic[key][0]) == 304:
            if int(dic[key][1]) >= 3:
                txt = 'Interface:  ' + str(key) +'  '+'    Error:   '+str(dic[key][0])
                sendMail(txt)

if __name__ == '__main__':
    main()