#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: threading_继承.py
@time: 2017/4/26 9:17
"""


import threading
import time
'''这种继承方式比较麻烦，建议不用这种'''
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n
    def run(self):
        print("Running task,",self.n)
        time.sleep(2)
t1 = MyThread("t1")
t2 = MyThread("t2")
t1.start()
t2.start()