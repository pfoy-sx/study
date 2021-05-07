#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: student.py
@time: 2017/4/6 21:36
"""


import sys
import os
BASICS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASICS_PATH)

from src import dbinit

class Student(object):
    '''学生类方法'''

    def __init__(self,schoolid):
        self.schoolID = schoolid
        self.init = dbinit.INITDB()
        self.S, self.SClist, self.STlist, self.SSlist, self.CClist = self.init.initdb(self.schoolID)
        self.SC = list(self.S[2])
        self.ST = list(self.S[3])
        self.SS = list(self.S[4])
    '''教师类方法'''

    def registered(self,studentid,studentname,classID):
        for i in self.SS:
            if studentid == i.split(':')[0]:
                print('该学生编号已存在')
                return False
        if classID in self.CClist:
            for i in self.ST:
                if classID == i.split(':')[4]:
                    new = studentid+':'+studentname+':'+i.split(':')[3]+':'+classID+':'+ '0'
                    self.SS.append(new)
                    self.S[4] = self.SS
                    self.init.save(self.schoolID, self.S, self.SC, self.ST, self.SS)
        else:
            print("班级不存在")

    def pay(self):
        self.status = 1


def main():
    while True:
        print('---------学生注册-----------')
        schoolID = input("输入你报校学校ID：").strip()
        try:
            student = Student(schoolID)
            print("该校可报课程有：")
            for i in student.SC:
                print("课程编号：%s 课程名称：%s 报名费用：%s 学习周期：%s" %(i.split(':')[0],i.split(':')[1],i.split(':')[2],i.split(':')[3]))
            print("开班信息：")
            for i in student.ST:
                print("教师：%s 课程编号：%s 班级：%s" % (i.split(':')[1],i.split(':')[3],i.split(':')[4]))
            studentid = input("输入你的ID：")
            studentname = input("输入你的名称：")
            classID = input("输入你报校班级ID：")
            student.registered(studentid,studentname,classID)

        except TypeError:
            print("没有该学校参数有误！")
