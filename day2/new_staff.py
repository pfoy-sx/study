#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/14 9:19
# @Author  : Beam
# @File    : new_staff.py
# 可进行模糊查询，语法至少支持下面3种:
# 　　select name,age from staff_table where age > 22
# 　　select  * from staff_table where dept = "IT"
#     select  * from staff_table where enroll_date like "2013"
# 查到的信息，打印后，最后面还要显示查到的条数
# 可创建新员工纪录，以phone做唯一键，staff_id需自增
# 可删除指定员工信息纪录，输入员工id，即可删除
# 可修改员工信息，语法如下:
# 　　UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
#  注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码

import datetime,time




#列表分割
def getdbinfo(i):
    INFODICT = {}
    INFODICT['staff_id'] = i.strip().split(',')[0]
    INFODICT['phone'] = i.strip().split(',')[1]
    INFODICT['name'] = i.strip().split(',')[2]
    INFODICT['age'] = i.strip().split(',')[3]
    INFODICT['dept'] = i.strip().split(',')[4]
    INFODICT['staff'] = i.strip().split(',')[5]
    INFODICT['date'] = i.strip().split(',')[6]
    return INFODICT


#返回一个初始化的数据字典
def info():
    list1 = []
    list2 = []
    with open(r'./staff.txt', 'r') as fn:
        for i in fn.readlines():
            try:
                key = i.strip().split(',')[1]
                value = getdbinfo(i)
                list1.append(key)
                list2.append(value)
            except:
                continue
    infodict = dict(map(lambda x, y: [x, y], list1, list2))
    return infodict

#装饰器检查有没有这个key,功能做失败
def check(func):
    dbinfo = info()
    def inner(*args, **kwargs):
        for key in dbinfo:
            if args == dbinfo[key][args]:
                func()
        else:
            print("员工表没有该信息，请核对！")
    return inner

#遍历dbinfo
def getinfo(dbinfo,dic):
    resultdict = {}
    n = 0
    if 'age' in dic.keys():
        for key in dbinfo:
            if int(dbinfo[key]['age']) > int(dic['age']):
                print(dbinfo[key])
                n += 1
        print('符合条件的共 %s 条'% n)
    elif 'dept' in dic.keys():
        for key in dbinfo:
            if dbinfo[key]['dept'] == dic['dept']:
                print(dbinfo[key])
                n += 1
        print('符合条件的共 %s 条'% n)
    elif 'date' in dic.keys():
        for key in dbinfo:
            value = dbinfo[key]['date'].split('-')[0]
            if dic['date'] == value:
                print(dbinfo[key])
                n += 1
        print('符合条件的共 %s 条'% n)


#匹配查询
def select(choose):
    dbinfo= info()
    postdict = {}
    if choose == '1':
        age = input("请输入你要查询多大的年龄段：")
        try:
            age = int(age)
            sql = 'select name,age from staff_table where age > %s'  % age
            postdict['age'] = int(age)
            getinfo(dbinfo,postdict)
        except ValueError:
            print("请输入一个整数")
    elif choose == '2':
        dept = input("请输入你要查询的部门：")
        sql = 'select * from staff_table where age > %s' % dept
        postdict['dept'] = dept
        getinfo(dbinfo, postdict)
    elif choose == '3':
        enroll_date = input("请输入入职年份")
        sql = "select  * from staff_table where enroll_date like '%s'" % enroll_date
        postdict['date'] = enroll_date
        getinfo(dbinfo, postdict)
    else:
        print("输入有误！")

#增加
def add():
    phone = input("请输入手机号码：")
    name = input("请输入名字：")
    age = input("请输入年龄：")
    dept = input("请输入部门：")
    staff = input("请输入薪酬：")
    date = input("请输入入职时间：")
    with open(r'./staff.txt','r') as f:
        lines = f.readlines()  #读取所有行
        last_line = lines[-1]  # 取最后一行
        staff_id = str(int(last_line.split(',')[0]) + 1)
    with open(r'./staff.txt','a') as f:
        s = staff_id+','+phone+','+name+','+age+','+dept+','+staff+','+date
        f.write(s+'\n')

#删除
#@check
def dele(staff_id):
    import shutil
    with open('./staff.txt', 'r') as f:
        with open('./staff.txt.new', 'w') as g:
            for line in f.readlines():
                if line.split(',')[0] != staff_id:
                    g.write(line)
    shutil.move('./staff.txt.new', './staff.txt')

#修改
#@check
def up(phone):
    name = input("请输入你要更改的名字：")
    age = input("请输入你要修改的年龄：")
    dept = input("请输入你要修改的部门：")
    staff = input("请输入你要修改的薪酬：")
    date = input("请输入你要修改的入职时间：")
    import shutil
    with open('./staff.txt', 'r') as f:
        with open('./staff.txt.new', 'w') as g:
            for line in f.readlines():
                if line.split(',')[1] != phone:
                    g.write(line)
    shutil.move('./staff.txt.new', './staff.txt')
    with open(r'./staff.txt','r') as f:
        lines = f.readlines()  #读取所有行
        last_line = lines[-1]  # 取最后一行
        staff_id = str(int(last_line.split(',')[0]) + 1)
    with open(r'./staff.txt','a') as f:
        s = staff_id+','+phone+','+name+','+age+','+dept+','+staff+','+date
        f.write(s+'\n')



def main():
    while True:
        contrl = input("1、查询   2、：增加   3、删除   4、修改    Q、退出 ：")
        if contrl.lower() == 'q':
            print('退出')
            exit()
        elif contrl == '1':
            choose = input("1、年龄匹配  2、部门匹配   3、入职年份匹配   Q、返回")
            if choose.lower() == 'q':
                break
            elif choose == '1' or choose == '2' or choose == '3':
                select(choose)
            elif choose == '1':
                select(choose)
                continue
            elif choose == '2':
                select(choose)
                continue
            elif choose == '3':
                select(choose)
                continue
            else:
                print('输入有误！')
                continue
        elif contrl == '2':
            add()
        elif contrl == '3':
            staff_id = input('请输入你要删除的员工id：')
            dele(staff_id)
        elif contrl == '4':
            phone = input('请输入你要修改的员工号码：')
            up(phone)
        else:
            print('输入有误！')

            continue



if __name__ == '__main__':
    main()