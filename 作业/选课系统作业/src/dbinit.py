#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: dbinit.py
@time: 2017/4/7 9:46
"""

import os,sys
BASICS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASICS_PATH)


import pickle
from config import setting

class INITDB(object):
    '''这个类用于数据的初始化、读取以及保存'''
    def __init__(self):
        if len(os.listdir(setting.schools_path)) == 0:
            print(self.create())

        # else:
        #     print("---------------初始化数据为---------------")
        #     print("第一所学校：%s" % self.initdb('S1'))
        #     print("第二所学校：%s" % self.initdb('S2'))

    def create(self):
        ##课程
        S1C1 = ['C1:linux:1000:5','C2:python:9000:20']  ##S1学校的课程列表：“课程id：课程名称：价格：周期”
        S2C1 = ['C1:go:5000:30']    ##S2学校的课程列表
        pickle.dump(S1C1,open(os.path.join(setting.course_path,'S1C1'),'wb'))   #记录到course数据库里
        pickle.dump(S2C1,open(os.path.join(setting.course_path,'S2C1'),'wb'))   #记录到course数据库里

        #教师
        S1T = ['T1:Alex:S1:C2:S1C1']   #教师列表：“教师编号：名称：学校id：课程id：班级ID”
        S2T  = ['T1:Wtl:S2:C3:S2C1']
        pickle.dump(S1T,open(os.path.join(setting.teachers_path,'S1T'),'wb'))
        pickle.dump(S2T,open(os.path.join(setting.teachers_path,'S2T'),'wb'))   #

        #学生
        S1S1 = ['stu1:Beam:C2:S1C1:90']  #学生列表：“学生编号：名称：课程id：班级ID：成绩”
        S2S1 = ['stu1:sb:C3:S2C1:0']
        pickle.dump(S1S1,open(os.path.join(setting.students_path,'S1S1'),'wb'))
        pickle.dump(S2S1,open(os.path.join(setting.students_path,'S2S1'),'wb'))

        #学校
        S1 = ['S1', '老男孩北京',S1C1 , S1T, S1S1]  #学校列表:“学校编号，名称，课程列表，教师列表，学生列表”
        S2 = ['S2', '老男孩上海',S2C1, S2T, S2S1]
        pickle.dump(S1,open(os.path.join(setting.schools_path,'S1'),'wb'))
        pickle.dump(S2,open(os.path.join(setting.schools_path,'S2'),'wb'))
        return "初始化成功！"

    def getList(self,S):
        SClist, STlist, SSlist, CClist = [],[],[],[]
        for i in self.S[2]:
            SClist.append(i.split(":")[0])
        for i in self.S[3]:
            STlist.append(i.split(":")[0])
        for i in self.S[4]:
            SSlist.append(i.split(":")[0])
        for i in self.S[3]:
            CClist.append(i.split(":")[4])
        return SClist, STlist, SSlist, CClist

    def initdb(self,schoolID):
        if schoolID == 'S1':
            with open(os.path.join(setting.course_path,'S1C1'),'rb') as FS1C1:
                self.SC = pickle.load(FS1C1)
            with open(os.path.join(setting.teachers_path,'S1T'),'rb') as FS1T:
                self.ST = pickle.load(FS1T)
            with open(os.path.join(setting.students_path, 'S1S1'), 'rb') as FS1S1:
                self.SS = pickle.load(FS1S1)
            with open(os.path.join(setting.schools_path,'S1'),'rb') as FS1:
                self.S = pickle.load(FS1)
            SClist,STlist,SSlist,CClist = self.getList(self.S)   #学校、解除个报告、教师、学生列表
            print("该学校信息：%s" % self.S)
            return self.S, SClist, STlist, SSlist, CClist

        elif schoolID == 'S2':
            with open(os.path.join(setting.course_path,'S2C1'),'rb') as FS2C1:
                self.SC = pickle.load(FS2C1)
            with open(os.path.join(setting.teachers_path,'S2T'),'rb') as FS2T:
                self.ST = pickle.load(FS2T)
            with open(os.path.join(setting.students_path,'S2S1'),'rb') as FS2S1:
                self.SS = pickle.load(FS2S1)
            with open(os.path.join(setting.schools_path,'S2'),'rb') as FS2:
                self.S = pickle.load(FS2)
            SClist, STlist, SSlist, CClist = self.getList(self.S)
            print("该学校信息：%s" % self.S)
            return self.S, SClist, STlist, SSlist, CClist



    def save(self,studentID,S,SC,ST,SS):
        if studentID == 'S1':
            print("Save S1")
            pickle.dump(SC,open(os.path.join(setting.course_path,'S1C1'),'wb'))   #记录到course数据库里
            pickle.dump(ST,open(os.path.join(setting.teachers_path,'S1T'),'wb'))
            pickle.dump(SS,open(os.path.join(setting.students_path,'S1S1'),'wb'))
            pickle.dump(S,open(os.path.join(setting.schools_path,'S1'),'wb'))
        elif studentID == 'S2':
            print("Save S2")
            pickle.dump(SC,open(os.path.join(setting.course_path,'S2C1'),'wb'))   #记录到course数据库里
            pickle.dump(ST,open(os.path.join(setting.teachers_path,'S2T'),'wb'))
            pickle.dump(SS,open(os.path.join(setting.students_path,'S2S1'),'wb'))
            pickle.dump(S,open(os.path.join(setting.schools_path,'S2'),'wb'))
        else:
            print("非法ID，Save失败")
