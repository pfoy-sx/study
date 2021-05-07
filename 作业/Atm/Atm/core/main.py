#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/20 10:51
# @Author  : Beam
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import os,sys
DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取父级根目录绝对路径
sys.path.append(DIR)    #把父级根目录加入到环境变量，可以导入该目录下其他子级模块

import sqlite3

#卡用戶狀態
USERLOGIN = {
    'username':None,
    'isFlag':False,
    'user_id':None,
    'balance':None,
    'status':None
}

#管理用戶狀態
ADMINLOGIN = {
    'user_id':None,
    'username':None,
    'passwd':None,
    'isFlag':False
}

#購物车狀態
BUYLISTDICT = {
    'sum':None,
    'status':False
}

ORDERDICT = {}

def select_DB(sql):
    import sqlite3
    conn = sqlite3.connect(r'../db/db.db')
    cur = conn.cursor()
    cursor =cur.execute(sql)
    return cursor


#獲取管理賬戶的信息帳號密碼id
def getAdminUserInfo(user):
    sql = "select * from t_user where user ='%s';" % user
    cur = select_DB(sql)
    try:
        for i in cur:
            user_id = i [0]
            user = i[1]
            passwd = i[2]
        return user_id,user,passwd
    except UnboundLocalError:
        return False

#获取用户卡账号密码以及id
def getUserInfo(user):
    sql = "select * from t_info where cardnum ='%s';" % user
    cur = select_DB(sql)
    try:
        for i in cur:
            cardname = i [0]
            passwd = i[1]
            user_id = i[2]
            balance = i[3]
            status = i[4]
        global USERLOGIN
        USERLOGIN['balance'] = balance
        if int(status) == 1:
            return False
        return cardname,passwd,user_id,balance,status
    except UnboundLocalError:
        return False


#银行卡登陆模块
def login():
    print('你还没有登陆，请先登陆！')
    while True:
        incardname = input('请输入八位卡号:')
        inpassword = input('请输入你的密码:')
        if not getUserInfo(incardname):
            print('没有该账户或帳號已凍結！！')
        else:
            if not USERLOGIN['isFlag']:
                cardname,passwd,user_id,balance,status = getUserInfo(incardname)
                if str(cardname) == incardname and str(passwd) == inpassword:   #int类型不能直接用==判断
                    print('登陆成功！')
                    USERLOGIN['username'] = cardname
                    USERLOGIN['passwd'] = passwd
                    USERLOGIN['user_id'] = user_id
                    USERLOGIN['balance'] = balance
                    USERLOGIN['status'] = status
                    USERLOGIN['isFlag'] = True
                    return True
                else:
                    print('密码错误，请重新登陆！')
            else:
                break

#管理员装饰器
def adminouter(func):
    def inner(*args,**kwargs):
        if  ADMINLOGIN['isFlag']:
            func()
        else:
            adminLogin()
    return inner

#管理员登陆模块
def adminLogin():
    while True:
        incardname = input('请输管理賬戶:')
        inpassword = input('请输管理密码:')
        if not getAdminUserInfo(incardname):
            print('没有该账户！')
        else:
            if not ADMINLOGIN['isFlag']:
                user_id,user,passwd = getAdminUserInfo(incardname)
                if str(user) == incardname and str(passwd) == inpassword:   #int类型不能直接用==判断
                    print('登陆成功！')
                    ADMINLOGIN['username'] = user
                    ADMINLOGIN['passwd'] = passwd
                    ADMINLOGIN['user_id'] = user_id
                    ADMINLOGIN['isFlag'] = True
                    return True
                else:
                    print('密码错误，请重新登陆！')
            else:
                break

##判断是否登陆了，登陆了继续运行，否则切换到登陆
def outer(func):
    def inner(*args,**kwargs):
        if  USERLOGIN['isFlag']:
            func()
        else:
            login()
    return inner


#获取购物车商品
def getBuylist():
    from core import shopping
    try:
        orderlist,orderprice = shopping.buyList()
        global ORDERDICT,BUYLISTDICT
        ORDERDICT = dict(map(lambda x,y:[x,y],orderlist,orderprice))
        BUYLISTDICT['status'] = True
        BUYLISTDICT['sum'] = sum(orderprice)
    except:
        print('False')

#支付模块接口
@outer
def paying():
    from core import transaction
    if transaction.transaction(1,BUYLISTDICT['sum'],USERLOGIN):
        print('支付成功')
        with open(r'../logs/paying.log','a+') as fn:
            import time
            s = str(USERLOGIN['user_id']) + '  ' + str(USERLOGIN['username']) +'  '+ str(time.strftime("%Y-%m-%d %H:%M %p", time.localtime())) + '  ' + '购物清单:' + str(ORDERDICT) + '  '+ '总额:'+ str(BUYLISTDICT['sum'])  +'  支付成功!\n'
            fn.writelines(s)
        global BUYLISTDICT
        BUYLISTDICT['status'] = False
        BUYLISTDICT['sum'] = None
        getUserInfo(USERLOGIN['username'])
        return True
    else:
        print('支付失敗')
        return False

#提现模块接口
@outer
def getMomey():
    from core import transaction
    if transaction.transaction(2, USERLOGIN):
        getUserInfo(USERLOGIN['username'])
        return True

#查询当前银行卡的余额
@outer
def checkBalance():
    print('Your Balance:%s' % USERLOGIN['balance'])

#管理接口
@adminouter
#10:賬單查詢  11:添加賬戶   12:凍結賬戶   13:查詢名下賬戶   14:賬戶金額互轉   15:提現
def manager():
    # 10:賬單查詢  11:添加賬戶   12:凍結賬戶   13:查詢名下賬戶   14:賬戶金額互轉   15:提現  Q:退出
    while True:
        try:
            print('10:賬單查詢  11:添加賬戶   12:凍結名下賬戶   13:查詢名下賬戶   14:賬戶金額互轉  Q:退出')
            choose = input('请输入你的选择：')
            if choose.lower() == 'q':
                break
            elif int(choose) not in [10,11,12,13,14]:
                print('输入错误，请重新选择！')
                continue
            else:
                from core import transaction
                transaction.Manager(int(choose),ADMINLOGIN)
                continue
        except ValueError:
            print('请输入正确的选项！')
            continue


def run():
    while True:
        print('1:购物  2：支付   3：余额查询  4:提现  5：管理中心  6：退出登录   Q:退出')
        control = input('请输入你的选择：')
        if control == '1':
            getBuylist()
            continue
        elif control == '2':
            if not BUYLISTDICT['status']:
                print('您還沒有購物，請先購物！')
                continue
            else:
                paying()
                continue
        elif control == '3':
            checkBalance()
            continue
        elif control == '4':
            getMomey()
            continue
        elif control == '5':
            manager()
            continue
        elif control == '6':
            global USERLOGIN,ADMINLOGIN
            USERLOGIN['isFlag'] = False
            ADMINLOGIN['isFlag'] = False
        elif control.lower() == 'q':
            sys.exit(1)
        else:
            print('输入有误，请重新输入')


if __name__ == '__main__':
    run()