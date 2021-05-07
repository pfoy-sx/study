#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: class_chose.py
@time: 2017/3/26 17:02
"""
'''
school   -> teachers教师、class班级、curriculum课程(cost费用)、student学生
schooID:{teachers:{teacher1,teacher2,},classes:{classname1,classname2,},curriculums:{curid1:{curriculumname1:cost},curid2:{curriculumname1:cost},},student:{stud1,stud2,}}
teachers -> class班级、curriculum课程、student学生、achievement成绩
teachers:{teacherID:{name:XXX,curriculum:XXX,classname:xxxx},}
student  -> register注册、class班级、payment缴费

#字典格式
{
school:{
        teachers:[tea1:{students:[stu1:{achievement:?}],curriculum},]      
        schoolclass:{ students:[]}      
        teacount:none
        curriculum:[]
        }
}
'''

import pickle

class CtrlAll(object):
    '''基类，只用于pickle，给子类继承'''
    def __init__(self):

        #获取pickle加载，school列表，teacher列表，学生列表
        self.SCHOOLID = pickle.load('./school.pick')
        self.TEACHERSID = pickle.load('./teachers.pick')
        self.STUDENTSID = pickle.load('./students.pick')

class school(CtrlAll):
    '''学校类'''
    teacount = 0
    def createSchool(self, schoolID, schoolname):
        '''构造方法，初始化学校ID、学校、课程'''
        self.schoolID = schoolID
        self.schoolname = schoolname
        self.schools = {}
        self.schools[schoolID] = schoolname
        global SCHOOLID

    def createTeachers(self,teacherID,teachername,curriculum,teachclass):
        '''创建教师ID,教师，创建对应课程以及班级'''
        self.teacherID = teacherID
        self.teachersname = teachername
        self.curriculum = curriculum
        self.teachclass = teachclass
        self.teacount+=1
    def createCurriculum(self,curriculum,tuition):
        '''创建课程，包括课程名、课程费用'''
        self.curriculum = curriculum
        self.tuition = tuition
    def createClass(self,classname):
        '''创建班级'''
        self.classname = classname


class teachers(CtrlAll):
    def __init__(self,teachersname):
        #认证是否有该教师
        self.teachersname = teachersname


class students(CtrlAll):
    pass


def main():
    s = school()
    print(s.SCHOOLID)
    # while True:
    #     SCHOOLID,TEACHERSID,STUDENTSID = CtrlAll()
    #     role = input("角色选择(1：学校；2：教师；3：学生):")
    #     auth = input("输入认证码（ID）：")
    #     if role == '1' and auth in SCHOOLID:
    #         admin = school()
    #         print("认证成功！")
    #         pass
    #     elif role == '1' and auth not in SCHOOLID:
    #         print("没有该学校")
    #         print("======创建学校======")
    #         admin = school()
    #         schoolid = input("请输入学校认证码(Sample:S001)：")
    #         schoolname = input("请输入学校名称：")
    #         if schoolid in SCHOOLID:
    #             print('该ID已存在')
    #             continue
    #         admin.createSchool('schoolID','schoolname')
    #
    #     elif  role == '2' and auth in TEACHERSID:
    #         teacher = teachers(auth)
    #         pass
    #     elif role == '3' and auth in STUDENTSID:
    #         student = students(auth)
    #         pass
    #     elif role == '3' and auth not in STUDENTSID:
    #         #调用学生类接口注册
    #         pass
    #     else:
    #         print("该角色用户不存在！")


if __name__ == '__main__':
    main()