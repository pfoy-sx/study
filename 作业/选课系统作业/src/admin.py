#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: admin.piuy
@time: 2017/4/6 9:31
"""

import sys
import os
BASICS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASICS_PATH)

from src import dbinit

class School(object):

    def __init__(self,schoolid):
        self.schoolID = schoolid
        self.init = dbinit.INITDB()
        self.S, self.SClist, self.STlist, self.SSlist, self.CClist = self.init.initdb(self.schoolID)
        self.SC = list(self.S[2])
        self.ST = list(self.S[3])
        self.SS = list(self.S[4])
        # print(self.S)
        # print(self.SC)
        # print(self.ST)
        # print(self.SS)

    def createTeacher(self,teacherID,teachername,courseid):

        '''创建教师编号，名称，课程id'''
        self.teacherID = teacherID
        self.teachername = teachername
        self.courseid = courseid
        #self.classid = classid
        if not self.teacherID in self.STlist:
            if self.courseid in self.SClist:
                self.strST= '%s:%s:%s:%s:%s' %(self.teacherID,self.teachername, self.schoolID, self.courseid,"None")
                self.ST.append(self.strST)
                self.S[3] = self.ST
                self.init.save(self.schoolID, self.S, self.SC, self.ST, self.SS)
            else:
                print("课程不存在！")
        else:
            print("教师编号已存在！")

    def createCourse(self,courseID,coursename,courseprice,coursecycle):
        '''创建课程，名称、价格、周期'''

        self.courseID = courseID
        self.coursename = coursename
        self.courseprice = courseprice
        self.coursecycle = coursecycle
        self.strSC= '%s:%s:%s:%s' %(self.courseID,self.coursename, self.courseprice,self.coursecycle)
        self.SC.append(self.strSC)
        self.S[2] = self.SC
        self.init.save(self.schoolID,self.S,self.SC,self.ST,self.SS)

    def createClass(self,classID,courseID,teacherID):
        '''创建班级，对应的课程ID和老师ID'''
        self.classID = classID
        self.courseID = courseID
        self.teacherID = teacherID
        status = 0
        if self.classID in self.CClist:
            print("班级已存在!")
            status = 1
        if status == 0 :
            if self.courseID in self.SClist and self.teacherID in self.STlist:
                for i in self.ST:
                    if i.split(':')[0] == self.teacherID and i.split(':')[4] == 'None':
                        print("该教师可以授课！")
                        new = i.split(':')[0] + ':' + i.split(':')[1] + ':' + i.split(':')[2] + ':' + i.split(':')[3] + ':' + self.classID
                        print(new)
                        self.ST.remove(i)
                        self.ST.append(new)
                        print(self.ST)
                        self.S[3] = self.ST
                        self.init.save(self.schoolID, self.S, self.SC, self.ST, self.SS)
            else:
                print("输入有误，请确保该教师还没有带班以及学校有该门课程！")
        else:
            return False




def main():
    while True:
        schoolid = input("输入你要管理的学校ID：").strip()
        try:
            admin = School(schoolid)
            print('''
            1.创建教师
            2.创建课程
            3.创建班级''')
            choose = input("请输入你的选择（Q退出）")
            if choose.strip() == '1':
                teacherID = input("输入教师ID：")
                teachername = input("输入教师名称：")
                courseid = input("输入课程ID：")
                #classid = input("输入班级ID：")
                admin.createTeacher(teacherID,teachername,courseid)
            elif choose.strip() == '2':
                courseID = input("输入课程ID：")
                coursename = input("输入课程名称：")
                courseprice = input("输入课程价格：")
                coursecycle = input("输入课程学习周期：")
                admin.createCourse(courseID, coursename, courseprice, coursecycle)
            elif choose.strip() == '3':
                classID = input("输入班级ID：")
                courseID = input("输入课程ID：")
                teacherID = input("输入授课教师ID：")
                admin.createClass(classID,courseID,teacherID)
            elif choose.strip().lower() == 'q':
                exit()
            else:
                print("输入有误！")
        except TypeError:
            print("传递参数有误！")

    # elif schoolid == init.S2[0]:
    #     print("该校信息：%s" % init.S2)
    # else:
    #     print("学校不存在")


