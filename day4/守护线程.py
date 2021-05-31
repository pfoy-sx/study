#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: 守护线程.py
@time: 2017/4/26 17:19
"""
import threading
import time

def run(n):
    print('task',n)
    time.sleep(2)
starttime = time.time()
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" % i,))   #新建线程，taarget后面跟函数名，args后面跟需要传递的惨，注意每个参要用,分隔
    t.setDaemon(True)    #把当前线程转变为守护线程，不会等待守护线程结束才结束
    t.start()

print('Cost : %s to thread all finshing'% (time.time() - starttime))