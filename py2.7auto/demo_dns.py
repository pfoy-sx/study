#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/13 10:30
# @Author  : Beam
# @Site    : 实现查询域名的A记录
# @File    : demo_dns.py
# @Software: PyCharm

import dns.resolver

def getArember(domain):
    """
    仅查询二级域名，顶级域名则出错
    :param domain:
    :return:打印该域名下的所有A记录
    """
    A = dns.resolver.query(domain,'A')   #指定查询A记录
    print '-----------------------A记录-----------------------'
    for i in A.response.answer:     #通过response.answer方法获取查询回应的信息
        for j in i:
            print j
    print '-----------------------分割线-----------------------'

def getMXrember(domain):
    """
    仅限输入一级域名（顶级域名），否则出错
    :param domain:
    :return:打印该域名下的所有MX记录
    """
    MX = dns.resolver.query(domain,'MX')   #指定查询MX记录
    print '-----------------------MX记录-----------------------'
    for i in MX:     #遍历回应结果，输出MX记录的preference以及exchanger信息
        print "MX preference =", i.preference,"MX exchanger =",i.exchange
    print '-----------------------分割线-----------------------'

def getNsrember(domain):
    """
    仅限输入一级域名（顶级域名），否则出错
    :param domain:
    :return: 打印该域名的NS记录值
    """
    ns = dns.resolver.query(domain,'NS')
    print '-----------------------NS记录-----------------------'
    for i in ns.response.answer:
        for j in i.items:
            print j.to_text(),
    print ''
    print '-----------------------分割线-----------------------'

def getCnamerember(domain):
    """
    仅限输入二级域名，否则出错
    :param domain:
    :return: 打印该域名的cname记录值
    """
    cname = dns.resolver.query(domain,'CNAME')
    print '-----------------------CNAME记录-----------------------'
    for i in cname.response.answer:
        for j in i.items:
            print j.to_text()
    print '-----------------------分割线-----------------------'

print '查询顶级域名输出MX、NS记录，查询耳机域名输出A、CNAME记录'
domain = raw_input('Please input an domain:')
if len(domain.strip().split('.')) == 2:
    getMXrember(domain)
    getNsrember(domain)
else:
    getArember(domain)
    getCnamerember(domain)
