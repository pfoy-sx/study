#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: setting.py
@time: 2017/4/7 9:34
"""
import os
#程序目录
BASICS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASICS_PATH, 'db')

course_path = os.path.join(DB_PATH, 'course')
schools_path = os.path.join(DB_PATH, 'schools')
students_path = os.path.join(DB_PATH, 'students')
teachers_path = os.path.join(DB_PATH, 'teachers')