#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: threading_ex1.py
@time: 2017/4/26 9:09
"""

import threading
import time
'''算出50个线程运行时间'''
def run(n):
    #print('task',n)
    time.sleep(2)
starttime = time.time()
t_obj = []
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" % i,))   #新建线程，taarget后面跟函数名，args后面跟需要传递的惨，注意每个参要用,分隔
    t.start()
    t_obj.append(t)
for t in t_obj:
    t.join()     #等待线程的结束
print('Cost : %s to thread all finshing'% (time.time() - starttime))