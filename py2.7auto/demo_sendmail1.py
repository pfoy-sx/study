#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/17 14:38
# @Author  : Beam
# @Site    : 
# @File    : demo_sendmail1.py
# @Software: PyCharm

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = 'smtp.126.com'   ##定义SMTP主机
SUBJECT = '官网业务质量周报'   ##邮件主题
TO = ['506556658@qq.com','beam.l@xuehu365.com']  ##收件地址
FROM = 'a506556658@126.com'    ##发件地址

def addimg(src,imgid):
    """
    :param src:图片路径
    :param imgid: 图片id
    :return:msgImage
    """
    with open(src,'rb') as fp:   #打开文件
        msgImage = MIMEImage(fp.read())   #创建MIMEImage对象，读取图片内容作为参数
    msgImage.add_header('Content-ID',imgid)    #指定图片文件的Content-ID,<img>标签src用到
    return msgImage

msg = MIMEMultipart('related')  ##创建MIMEMultipart对象,采用related定义内嵌资源的邮件体
msgtext = MIMEText("<font color=red>官网业务周平均演示图表：<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>","html","utf-8")  ##创建一个MIMEText对象，HTML元素包括文字与图片<img>
msg.attach(msgtext)   ##MIMEMultipart 对象附加MIMEText的内容
msg.attach(addimg("img/weekly.png","weekly"))  ##MIMEMultipart 对象附加MIMEImage的内容
attach = MIMEText(open("doc/week_report.xlsx","rb").read(),"base64","utf-8")   ##创建一个MIMEText对象，附加week_report.xlsx文档
attach["Content-Type"] = "application/octet-stream"    ##指定文件格式类型
attach["Content-Disposition"] = "attachment;filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("gb18030")   ##为保证中文文件名不出现乱码，对文件名进行编码转换

msg.attach(attach)      ##MIMEMultipart 对象附加MIMEText的内容
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
try:
    server = smtplib.SMTP()   ##创建smtp()对象
    server.connect(HOST,25)   ##通过connenct方法链接smtp主机
    server.starttls()         ##启动安全传输模式
    server.login("a506556658@126.com","506556658@qq.com")    ##邮箱账号登录校验
    server.sendmail(FROM,TO,msg.as_string())    ##邮件发送
    server.quit()    ##断开smtp链接
    print '邮件发送成功'
except Exception,e:
    print "失败：" + str(e)

