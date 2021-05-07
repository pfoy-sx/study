#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/20 14:07
# @Author  : Beam
# @File    : last_staff.py

#select * from t_staff where id = 1

#全局列表，用于匹配关键词
OPTCRUXS = ['select','update','delect','insert','from t_staff where']
FIELD = ['staff_id','phone','name','age','dept','staff','enroll_date']

# #全局字典，用于循环时临时存的位置
# INFODICT = {
#     'staff_id':None,
#     'phone':None,
#     'name':None,
#     'age':None,
#     'dept':None,
#     'staff':None,
#     'enroll_date':None
# }

#命令拆分
def analysisCommad(commad):
    import re
    try:
        temps = re.search('(.*)(from t_staff where)(.*)', commad).group(1).strip()
        optcrux = temps.strip().split(' ')[0]
        field = temps.strip().split(' ')[1]
        optcrux2 = re.search('(.*)(from t_staff where)(.*)', commad).group(2).strip()
        condition = re.search('(.*)(from t_staff where)(.*)', commad).group(3).strip()
        return optcrux,field,optcrux2,condition
    except AttributeError:
        a,b,c,d = False,False,False,False
        return a,b,c,d

#字段条件分析
def fieldGrammar(b):
    fields = []
    fields = b.split(',')
    for i in fields:
        if i == '*' and len(fields) == 1:
            return True
        else:
            if i in FIELD:
                return True
            else:
                return False

#语法分析
def judgeGrammar(a,b,c,d):
    if a not in OPTCRUXS or c not in OPTCRUXS:
        return False
    else:
        return True


#写入文本
def writeTxt(infolists,infodict):
    with open(r'./staff.txt','w') as fn:
        for i in infolists:
             fn.writelines(infodict[i]['staff_id']+','+infodict[i]['phone']+','+infodict[i]['name']+','+infodict[i]['age']+','+infodict[i]['dept']+','+infodict[i]['staff']+','+infodict[i]['enroll_date']+'\n')
        #print(infodict[i]['staff_id']+','+infodict[i]['phone']+','+infodict[i]['name']+','+infodict[i]['age']+','+infodict[i]['dept']+','+infodict[i]['staff']+','+infodict[i]['enroll_date']+'\n')

def select(b,d,infolists,infodict):
    pass


def insert(b,d,infolists,infodict):
    dict = {}
    staff_id = int(infolists[-1]) + 1
    phone = input("请输入手机号码：")
    name = input("请输入名字：")
    age = input("请输入年龄：")
    dept = input("请输入部门：")
    staff = input("请输入薪酬：")
    enroll_date = input("请输入入职时间：")
    dict['phone'] = phone
    dict['name'] = name
    dict['age'] = age
    dict['dept'] = dept
    dict['staff'] = staff
    dict['enroll_date'] = enroll_date
    infodict[str(staff_id)] = dict
    infolists.append(staff_id)
    writeTxt(infolists,infodict)

def update(b,d,infolists,infodict):
    print(b, d, infolists, infodict)

def delect(b,d,infolists,infodict):
    print(b, d, infolists, infodict)

#执行不同的命令
def choose(optcrux,b,c,d,infolists,infodict):
    if optcrux == 'select':
        print('select')
        select(b,d,infolists,infodict)
    elif optcrux == 'insert':
        print('insert')
        insert(b,d,infolists,infodict)
    elif optcrux == 'update':
        print('update')
        update(b,d,infolists,infodict)
    elif optcrux == 'delect':
        print('delect')
        delect(b,d,infolists,infodict)
    else:
        print('语法错误！')

def __init__():
    """[1:{},2:{},3:{} ....]"""
    infolists = []
    infodict = {}
    with open(r'./staff.txt','r') as fn:
        for i in fn.readlines():
            try:
                INFODICT = {}
                INFODICT['staff_id'] = i.strip().split(',')[0]
                INFODICT['phone'] = i.strip().split(',')[1]
                INFODICT['name'] = i.strip().split(',')[2]
                INFODICT['age'] = i.strip().split(',')[3]
                INFODICT['dept'] = i.strip().split(',')[4]
                INFODICT['staff'] = i.strip().split(',')[5]
                INFODICT['enroll_date'] = i.strip().split(',')[6]
                infodict[i.strip().split(',')[0]] = INFODICT
                infolists.append(i.strip().split(',')[0])
            except IndexError:
                continue
    return infolists,infodict


def main():
    #while True:
    infolists,infodict = __init__()
    print(infolists,infodict)
    #commad = input('请输入SQL命令:').lower()
    commad = 'insert name,id from t_staff where id = 1'
    a,b,c,d = analysisCommad(commad)
    fiel1 = judgeGrammar(a,b,c,d)
    fiel2 = fieldGrammar(b)
    if fiel1 and fiel2:
        choose(a,b,c,d,infolists,infodict)
        #writeTxt(infolists, infodict)
    else:
        print("语法错误")
        #continue

if __name__ == '__main__':
    main()