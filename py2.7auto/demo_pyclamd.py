#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/24 11:31
# @Author  : Beam
# @Site    : 
# @File    : demo_pyclamd.py
# @Software: PyCharm

#!/usr/bin/env python
#coding:utf8

import time
import pyclamd
from threading import Thread

class Scan(Thread):
    def __init__(self,IP,scan_type,file):
        """构造方法，参数初始化"""
        Thread.__init__(self)
        self.IP = IP
        self.scan_type = scan_type
        self.file = file
        self.connstr = ""
        self.scanresult = ""

    def run(self):
        """多线程run方法"""
        try:
            cd = pyclamd.ClamdNetworkSocket(self.IP,3310) #创建网络套接字连接对象
            if cd.ping():    #检测连通性
                self.connstr = self.IP + " connection [OK]"
                cd.reload()
                if self.scan_type == "contscan_file":   #选择不同的扫描方式
                    self.scanresult="{0}\n".format(cd.contscan_file(self.file))
                elif self.scan_type == "multiscan_file":
                    self.scanresult="{0}\n".format(cd.contscan_file(self.file))
                elif self.scan_type == "scan_file":
                    self.scanresult="{0}\n".format(cd.scan_file(self.file))
                time.sleep(1)
            else:
                self.connstr = self.IP + " connect error ,exit!"
                return
        except Exception,e:
            self.connstr = self.IP+" "+str(e)

IPs = ['10.24.153.84','10.117.198.19']   #需要扫描主机的列表
scantype = "multiscan_file"    #指定扫描模式，支持multiscan_file、contsccan_file、scan_file
scanfile = "/data"       #指定扫描路径
i = 1
threadnum = 4 #启动线程数
scanlist = [] #存储扫描scan类线程对象列表

for ip in IPs:
    currp = Scan(ip,scantype,scanfile) #创建扫描scan类对象，参数（ip、扫描模式，扫描路径）
    scanlist.append(currp)  #追加对象到列表
    if i%threadnum == 0 or i == len(IPs):   #当达到指定的线程数或IP列表数后启动、退出线程
        for task in scanlist:
            task.start()   #启动线程
        for task in scanlist:
            task.join()
            print task.connstr
            print task.scanresult
        scanlist = []
    i += 1
#with open('/tmp/EICAR','w') as fd:
#    fd.write(cd.EICAR())











