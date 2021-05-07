#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/9 15:00
# @Author  : Beam
# @Site    : 
# @File    : login.py
# @Software: PyCharm
#装饰器应用

LOGIN_INFO = {'status':False}

def outer(func):
    def inner(*args,**kwargs):
        if  LOGIN_INFO['status']:
            func()
        else:
            login()
    return inner

def checkAdmin(func):
    pass

@outer
def getInfo():
    print("欢迎%s登录管理系统" % LOGIN_INFO['user'])
    print("你的用户名是：%s" % LOGIN_INFO['user'])
    print("你的密码是：%s" % LOGIN_INFO['pwd'])

@outer
def login():
    if not LOGIN_INFO['status']:
        user = input("输入你的用户名：")
        pwd = input("输入你的密码：")
        if user == 'Beam' and pwd == '123456':
            LOGIN_INFO['user'] = user
            LOGIN_INFO['pwd'] = pwd
            LOGIN_INFO['status'] = True
            print("登录成功")
        else:
            print("验证失败！")
            return False
    else:
        print("你已经登录成功，无需重复登录")

def main():
    while True:
        contrl = input("请选择（1：管理系统 2：登录 3：退出）：")
        if int(contrl) == 1:
            getInfo()
        elif int(contrl) == 2:
            login()
        elif int(contrl) == 3:
            exit()
        else:
            print("出现未知错误")

if __name__ == '__main__':
    main()