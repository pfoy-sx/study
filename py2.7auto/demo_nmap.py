#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/24 15:19
# @Author  : Beam
# @Site    : 
# @File    : demo_nmap.py
# @Software: PyCharm

import sys
import nmap

scan_row = []
input_data = raw_input('Please input hosts and port:')
scan_row = input_data.split(" ")
if len(scan_row) != 2:
    print "Input errors,example \"192.168.1.0/24 80,443,22\""
    sys.exit(0)
hosts = scan_row[0]
prot = scan_row[1]
print scan_row

try:
    nm = nmap.PortScanner()   #创建端口扫描对象nm
except nmap.PortScannerError:
    print "Nmap not found", sys.exc_info()[0]
    sys.exit(0)
except:
    print "Unexpected error:", sys.exc_info()[0]
    sys.exit(0)

try:
    nm.scan(hosts=hosts, arguments=' -v -sS -p ' + port)
except Exception, e:
    print "Scan erro:" + str(e)

for host in nm.all_hosts():
    print "--------------------------------------------------------------"
    print 'Host:%s (%s)' % (host, nm[host].hostname())   #输出主机及主机名
    print 'State : %s' % nm[host].state()    #输出主机状态

    for proto in nm[host].all_protocols():   #遍历扫描协议，如tcp、udp
        print "--------------------------------------------------------------"
        print 'Protocol : %s' % proto   #输入协议名

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:   #遍历端口及输出端口与状态
            print 'port : %s\tstate : %s' % (port,nm[host][proto][port]['state'])



