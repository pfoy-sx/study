#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/28 10:20
# @Author  : Beam
# @Site    : 
# @File    : connect.py
# @Software: PyCharm



#为什么当调用公共配置这里的函数方法会报错，当执行execute(sql)说没有这个表？求解～！
def select_DB(sql):
    import sqlite3
    conn = sqlite3.connect(r'./db.db')
    cur = conn.cursor()
    cursor =cur.execute(sql)
    return cursor

def update_DB(sql):
    import sqlite3
    conn = sqlite3.connect(r'./db.db')
    print(sql)
    conn.execute(sql)
    conn.commit()
    conn.close()
    return True

# sql = "select * from t_user where user = 'beam'"
# cur = select_DB(sql)
# for i in cur:
#     print(i)