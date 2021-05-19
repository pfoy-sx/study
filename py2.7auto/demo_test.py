#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/13 16:45
# @Author  : Beam
# @Site    : 
# @File    : demo_test.py
# @Software: PyCharm

list = []
with open('./1.txt') as fd:
    for i in fd.readlines():
        list.append(i.strip())


print list