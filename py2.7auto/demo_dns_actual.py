#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/13 11:23
# @Author  : Beam
# @Site    : DNS域名轮训业务监控
"""
通过DNS轮询技术可以做多一个域名多赢多个IP实现简单高效的负载均衡，该脚本主要用途监控业务是否可用
本脚本以谷歌为例，在实际自行搭建的dns服务器只有纯IP
"""
# @File    : demo_dns_actual.py
# @Software: PyCharm

import dns.resolver
import os
import httplib

iplist = []   #定义IP列表变量
appdomain = "www.beam.pub" #定义业务域名

def  get_iplist(domain=''):
    """
    域名解释函数，解释成功的A记录的IP追加到iplist列表中
    :param domain:
    :return:
    """
    try:
        A = dns.resolver.query(domain,'A') ##解析域名的A记录
    except Exception,e:
        print "dns resolver error: " + str(e)
        return False
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    """
    checkip函数用于检查IP是否能正常打开，其实还能用curl -I 得到状态码来测试业务是否正常
    :param ip:
    :return:
    """
    checkurl = ip + ':80'   #定义要检测的IP地址
    getcontent = ''
    httplib.socket.setdefaulttimeout(5)   ##定义HTTP连接超时时间为5秒
    conn = httplib.HTTPConnection(checkurl)  ##创建http连接对象
    try:
        conn.request("GET","/",headers = {"HOST":appdomain})   ##发起URL请求，添加host主机头
        r = conn.getresponse()
        getcontent  = r.read(15)     ##获取URL页面前15个字符，用于做可用性校验
        print getcontent
    finally:
        if getcontent.lower() == '<!doctype html>':   ##监控url页的内容一般是实现定义好的，比如http200等
            print ip + ' [OK]'
        else:
            print ip + ' [Error]'

if __name__ == '__main__':
    if get_iplist(appdomain) and len(iplist)> 0 :
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error"

