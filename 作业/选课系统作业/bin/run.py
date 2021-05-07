#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: run.py
@time: 2017/4/7 9:22
"""

import sys
import os
BASICS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASICS_PATH)

from src import admin
from src import teacher
from src import student
from src import dbinit



while True:
    print('''
    1.管理视图
    2.教师视图
    3.学员视图
    ''')

    choose = input("请输入你的选择：")
    if choose.strip() == '1':
        admin.main()
    elif choose.strip() == '2':
        teacher.main()
    elif choose.strip() == '3':
        student.main()
    elif choose.lower().strip() == 'q':
        sys.exit(1)
    else:
        print("输入有误！请重新输入！")