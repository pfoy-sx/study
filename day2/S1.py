#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/14 15:49
# @Author  : Beam
# @Site    : 
# @File    : S1.py
# @Software: PyCharm


#斐波拉契

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield(b)
        a,b = b,a+b    #b赋值给a   ，a+b的值赋值给b
        n = n + 1
    return 'done'

# fib_gen = fib(15)
# print(fib_gen.__next__())
# print(fib_gen.__next__())
# print('=====start print(Beagin in 3rd)======')
# for i in fib_gen:
#     print(i)

