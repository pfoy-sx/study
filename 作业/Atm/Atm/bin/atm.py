#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/20 10:51
# @Author  : Beam
# @Site    : 
# @File    : atm.py
# @Software: PyCharm

import os,sys
DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取父级根目录绝对路径
sys.path.append(DIR)    #把父级根目录加入到环境变量，可以导入该目录下其他子级模块

from core import main
main.run()



