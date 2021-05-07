#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/14 14:46
# @Author  : Beam
# @Site    :
# @File    : staff.py
# @Software: PyCharm

OPTCRUXS = ['select','update','delect','insert','from t_staff2 where']
FIELD = ['staff_id','phone','name','age','dept','staff','enroll_date']

#命令拆分
def analysisCommad(commad):
    import re
    try:
        temps = re.search('(.*)(from t_staff2 where)(.*)', commad).group(1).strip()
        optcrux = temps.strip().split(' ')[0]
        field = temps.strip().split(' ')[1]
        optcrux2 = re.search('(.*)(from t_staff2 where)(.*)', commad).group(2).strip()
        condition = re.search('(.*)(from t_staff2 where)(.*)', commad).group(3).strip()
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

def updateDB(sql):
    import sqlite3
    conn = sqlite3.connect(r'./staff.db')
    conn.execute(sql)
    conn.commit()
    conn.close()
    return True

def insertDB(sql):
    import sqlite3
    conn = sqlite3.connect(r'./staff.db')
    conn.execute(sql)
    conn.commit()
    conn.close()
    return True

def selectDB(sql):
    import sqlite3
    conn = sqlite3.connect(r'./staff.db')
    cur = conn.cursor()
    cursor =cur.execute(sql)
    return cursor

def __init__():
    """[1:{},2:{},3:{} ....]"""
    infolists = []
    infodict = {}
    sql = 'select * from t_staff2;'
    cursor = selectDB(sql)
    for i in cursor:
        print(i)

def select(sql):
    lis = []
    cursor = selectDB(sql)
    for i in cursor:
        lis.append(i)
        print(i)
    print('有关的信息有 %s 条!' % len(lis))

def insert(sql):
    insertDB(sql)

def update(sql):
    updateDB(sql)

def delect(sql):
    delect(sql)

#执行不同的命令
def choose(optcrux,sql):
    if optcrux == 'select':
        print('select')
        select(sql)
    elif optcrux == 'insert':
        print('insert')
        insert(sql)
    elif optcrux == 'update':
        print('update')
        update(sql)
    elif optcrux == 'delect':
        print('delect')
        delect(sql)
    else:
        print('语法错误！')

def main():
    #while True:
    #infolists,infodict = __init__()
    #sql = input('请输入SQL命令:').lower()
    sql = 'select * from t_staff2 where enroll_date like "2016";'
    a,b,c,d = analysisCommad(sql)
    fiel1 = judgeGrammar(a,b,c,d)
    fiel2 = fieldGrammar(b)
    if fiel1 and fiel2:
        choose(a,sql)
        #writeTxt(infolists, infodict)
    else:
        pass
        #print("语法错误")
        #continue
    #__init__()
if __name__ == '__main__':
    main()