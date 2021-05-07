#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/14 14:46
# @Author  : Beam
# @Site    :
# @File    : staff.py
# @Software: PyCharm

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

#隐藏功能
def selectall():
    sql = "select * from t_staff2"
    result = selectDB(sql)
    for i in result:
        print(i)

#查询员工信息
def selectStaff():
    name = input('输入你要查询的员工名字：')
    sql = "select * from t_staff2 where NAME = '%s'" % name
    sql2 = "select count(*) from t_staff2 where NAME = '%s'" % name
    cursor = selectDB(sql)
    cursor2 = selectDB(sql2)
    for i in cursor:
        print(i)
    for j in cursor2:
        result = j[0]
    print('有关%s的信息有 %s 条。' %(name,result))

#查询薪酬范围
def selectStaffall():
    staff = input('输入你要查询的薪酬在多小以上：')
    sql = "select * from t_staff2 where SALARY > %s" % int(staff)
    sql2 = "select count(*) from t_staff2 where SALARY > %s" % int(staff)
    cursor = selectDB(sql)
    cursor2 = selectDB(sql2)
    for i in cursor:
        print(i)
    for j in cursor2:
        result = j[0]
    print('薪酬范围在 %s 以上的有 %s 条。' %(staff,result))

#插入员工信息
def insertStaff():
    try:
        name = input("请录入员工名字：")
        age = input("请录入员工年龄：")
        dept =input("请录入员工部门：")
        salary = input("请录入员工薪酬：")
        if not type(int(age)) == type(1) and type(int(salary)) == type(1):
            print("年龄和薪酬必须是一个整数！")
        else:
            sql = "INSERT INTO t_staff2(NAME,AGE,DEPT,SALARY) VALUES ('%s',%s,'%s',%s);" %(name,age,dept,salary)
            insertDB(sql)
    except ValueError:
        print("录入有误，请确保年龄和薪酬必须是一个整数！")

#更新员工薪酬
def updateStaff():
    name = input("请输入要修改薪酬的员工名字(区分大小写)：")
    sql2 = "select count(*) from t_staff2 where NAME = '%s'" % name
    cursor2 = selectDB(sql2)
    for j in cursor2:
        result = j[0]
    if result == 0:
        print("没有该员工，请检查是否输入有误！")
    else:
        try:
            salary = input("请输入%s现在的薪酬：" % name)
            sql = "update t_staff2 set SALARY = %s where NAME = '%s';" % (int(salary),name)
        except ValueError:
            print("录入有误，请确保薪酬必须是一个整数！")

#删除员工信息
def deleteStaff():
    try:
        id = input("请输入你要删除的员工ID号（数据无价，请谨慎！）：")
        selectsql = "select count(*) from t_staff2 where staff_id = '%s'" % int(id)
        cursor = selectDB(selectsql)
        for i in cursor:
            result = i[0]
        if result == 0:
            print("没有该员工，请查询后再进行操作！")
        else:
            sql = "DELETE FROM t_staff2 WHERE staff_id = %s" % int(id)
            updateDB(sql)
            print("删除成功")
    except:
        print("输入有误，请重新输入！")


def main():
    while True:
        print("1.查询某员工信息   2.查询薪酬范围的员工  3.插入员工信息   4.更新员工薪酬   5.删除员工信息   Q.退出")
        choose  = input("请输入你的选择：")
        if choose.lower() == 'q':
            print("退出系统！")
            import sys
            sys.exit()
        elif choose == '1':
            selectStaff()
        elif choose == '2':
            selectStaffall()
        elif choose == '3':
            insertStaff()
        elif choose == '4':
            updateStaff()
        elif choose == '5':
            deleteStaff()
        #隐藏功能，查看表所有员工信息
        elif choose == '100':
            selectall()
        else:
            print("输入有误，请重新输入！")
            continue




if __name__ == '__main__':
    main()