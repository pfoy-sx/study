#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/14 17:59
# @Author  : Beam
# @Site    :
# @File    : demo_sendmail.py
# @Software: PyCharm

import smtplib
import string
from email.mime.text import MIMEText

def sendMail():
    HOST = 'smtp.126.com'   ##定义SMTP主机
    SUBJECT = 'Test email from python'   ##邮件主题
    TO = ['506556658@qq.com','beam.l@xuehu365.com']  ##收件地址
    FROM = 'a506556658@126.com'    ##发件地址
    msg = MIMEText("""    ##创建一个MIMEText对象，分别制定html内容、类型、字符编码
    <table width="800" border="0" cellspacing="0" cellpadding="4">
    <tr><td bgcolor="CECFAD" height="20" style="font-size:14px">*官网数据<a href="monitor.domain.com">更多>></a></td></tr>
    <tr><td bgcolor="EFEBDE" height="100" style="font-size:"13px">
    1）日访问量：<font color=red>152433</font>  访问次数：23651 页面浏览量：45123  点击数：523122  数据流量：504MB<br>
    2) 状态码信息：<br>
    &nbsp;&nbsp;500:105   404:3264   503:214<br>
    3) 访客浏览器信息 <br>
    </td></tr>
    </table>""","html","utf-8")
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = TO
    #BODY =string.join(("From: %s" %FROM,"To: %s" % TO, "Subject: %s" % SUBJECT,"",text),"\r\n")     ##组装sendmail方法的邮件主题内容，每段内容以\r\n进行分隔
    try:
        server = smtplib.SMTP()   ##创建smtp()对象
        server.connect(HOST,25)   ##通过connenct方法链接smtp主机
        server.starttls()         ##启动安全传输模式
        server.login("a506556658@126.com","506556658@qq.com")    ##邮箱账号登录校验
        server.sendmail(FROM,TO,msg.as_string())    ##邮件发送
        server.quit()    ##断开smtp链接
        print '邮件发送成功'
        return True
    except Exception,e:
        print "失败：" + str(e)
        return False


def main():
    #text = 'Python rules them all!'   ##邮件内容


    sendMail()

if __name__ == '__main__':
    main()