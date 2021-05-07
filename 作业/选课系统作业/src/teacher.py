#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: teacher.py
@time: 2017/4/6 9:53
"""

import sys
import os
BASICS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASICS_PATH)


from src import dbinit

class Teacher(object):
    def __init__(self,schoolid):
        self.schoolID = schoolid
        self.init = dbinit.INITDB()
        self.S, self.SClist, self.STlist, self.SSlist, self.CClist = self.init.initdb(self.schoolID)
        self.SC = list(self.S[2])
        self.ST = list(self.S[3])
        self.SS = list(self.S[4])
    '''教师类方法'''
    def studentList(self,teacherid):
        self.tcc = ''
        self.studes = []
        for i in self.ST:
            if teacherid ==  i.split(':')[0]:
                self.tcc = i.split(':')[4]
        if not self.tcc == 'None':
            for student in self.SS:
                if student.split(':')[3] == self.tcc:
                    #print( "编号：%s 名字：%s 课程：%s 班级：%s  成绩：%s"   % (student.split(':')[0],student.split(':')[1],student.split(':')[2],student.split(':')[3],student.split(':')[4]  ) )
                    self.studes.append(student)
                else:
                    pass
            return self.studes
        else:
            print("学校还没有分配班级给你带~~")
            return False

    def studentScore(self,studentid,source,studes):
        for i in studes:
            if studentid == i.split(':')[0]:
                new = i.split(':')[0] +':'+i.split(':')[1] +':'+i.split(':')[2] +':'+i.split(':')[3] +':'+source
                self.SS.remove(i)
                self.SS.append(new)
                self.S[4] = self.SS
                self.init.save(self.schoolID, self.S, self.SC, self.ST, self.SS)
            else:
                print("该学生ID不存在")

def main():
    while True:
        schoolID = input("输入你所属的学校ID：").strip()
        try:
            teacher = Teacher(schoolID)
            teacherid = input("输入你的教师ID认证：")
            if teacherid in teacher.STlist:
                print("认证成功：")
                print('''
                1.查看学生列表
                2.修改学生成绩''')
                choose = input("请输入你的选择（Q退出）：")
                if choose.strip() == '1':
                    studes = teacher.studentList(teacherid)
                    for student in studes:
                        print("编号：%s 名字：%s" % (student.split(':')[0], student.split(':')[1]))
                elif choose.strip() == '2':
                    studentid = input("输入你要修改成绩的学生ID：")
                    source = input("输入你修改的成绩：")
                    studes = teacher.studentList(teacherid)
                    teacher.studentScore(studentid,source,studes)
                elif choose.strip().lower() == 'q':
                    exit()
                else:
                    print("输入有误！")
            else:
                print("该教师不存在")
        except TypeError:
            print("传递参数有误！")
