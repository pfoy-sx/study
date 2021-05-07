#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/14 14:46
# @Author  : Beam
# @Site    : 
# @File    : decorator.py
# @Software: PyCharm



#需求：
#写一个装饰器，增加函数工功能：统计test1和test2的函数运行时间
import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time = float(time.time())
        func()
        stop_time = float(time.time())
        c = stop_time - start_time
        print('the func run time is '+ str(c))
    return warpper

@timmer
def test1():
    print('test1：')
    a = [ i*2 for i in range(50000000)]

@timmer
def test2():
    print('test2：')
    b = ( i*2 for i in range(50000000))


test1()
test2()