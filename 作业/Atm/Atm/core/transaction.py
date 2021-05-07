#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/28 14:29
# @Author  : Beam
# @Site    : 
# @File    : transaction.py
# @Software: PyCharm



def update_DB(sql):
    import sqlite3
    conn = sqlite3.connect(r'../db/db.db')
    conn.execute(sql)
    conn.commit()
    conn.close()
    return True

def insert_DB(sql):
    import sqlite3
    conn = sqlite3.connect(r'../db/db.db')
    conn.execute(sql)
    conn.commit()
    conn.close()
    return True

def select_DB(sql):
    import sqlite3
    conn = sqlite3.connect(r'../db/db.db')
    cur = conn.cursor()
    cursor =cur.execute(sql)
    return cursor

def getRandom():
    import random
    """
    生成一串6位数字
    :return:返回一个随机数字组成的字符串
    """
    li = []
    for i in range(8):
        temp = random.randrange(0,9)
        li.append(str(temp))
    result = ''.join(li)
    return result

#交易模塊
#1:支付   2:提現(手續費5%)  3:金額互轉
def transaction(choose,*args,**kwargs):
    if choose == 1:
        #args[0]是支付的金额，args[1]是银行卡登陆后的所有信息可直接打印args[1]['balance']
        if args[1]['balance'] >  args[0]:
            money = int(args[1]['balance']) - int(args[0])
            sql = "UPDATE t_info SET balance = %s WHERE cardnum = '%s';" % (money,args[1]['username'])
            if update_DB(sql):
                return True
            else:
                return False
        elif args[1]['balance'] <  args[0]:
            print('餘額不足')
            return False
        else:
            return False
    elif choose == 2:
        #args[0]是银行卡登陆后的所有信息可直接打印args[1]['balance']
        output = input('请输入你想提现的金额（提现手续费5%）：')
        try:
            if int(output) > args[0]['balance']:
                print('提现失败，余额不足！')
            else:
                current = int(args[0]['balance']) - (int(output) * 0.05 + int(output))
                sql = "UPDATE t_info SET balance = %s WHERE cardnum = '%s';" % (current,args[0]['username'])
                update_DB(sql)
                with open(r'../logs/withdrawals.log','a+') as fn:
                    import time
                    shouxufei = int(output) * 0.05
                    s = str(args[0]['username']) +'  '+ str(time.strftime("%Y-%m-%d %H:%M %p", time.localtime())) + '  提現:' + str(output)+'  手續費:'+ str(shouxufei) +'\n'
                    fn.writelines(s)
                return True
        except ValueError:
            print('只能提取整数金额！')
            return False
    else:
        return False


#管理模塊
#10:賬單查詢  11:添加賬戶   12:凍結賬戶   13:查詢名下賬戶   14:賬戶金額互轉   15:提現
# args[0]是管理员的账号密码ID的字典信息
def Manager(choose,*args,**kwargs):
    #调试使用，看传递过来的值
    #print(args)
    if choose == 10:
        print('用户：%s 您好，你的名下账单如下（卡号：购物时间：清单：总额）：'% args[0]['username'])
        with open(r'../logs/paying.log') as fn:
            for i in fn.readlines():
                if i.startswith(str(args[0]['user_id'])):
                    print(i.split()[1:-1])
        print('------------------------------------------分割线------------------------------------------')
        return True
    elif choose == 11:
        s = int(getRandom())
        sql = "INSERT INTO t_info (cardnum,cardpwd,user_id,balance,status)VALUES (%s, '123456', %s, 16000, 0 );"%(s,args[0]['user_id'])
        insert_DB(sql)
        print('您的新卡号是：%s ,默认密码：123456，账户默认开户金额16000' % s)
        with open(r'../logs/operation.log','a+') as fn:
            neirong = str(args[0]['username']) + '  ' + str(args[0]['user_id']) + '  '+ '新增卡号：'+str(s) +'\n'
            fn.writelines(neirong)
        return True
    elif choose == 12:
        sql = "UPDATE t_info SET status = 1 WHERE user_id = %s;" % int(args[0]['user_id'])
        print(sql)
        update_DB(sql)
        with open(r'../logs/operation.log','a+') as fn:
            neirong = str(args[0]['username']) + '  ' + str(args[0]['user_id']) + '  '+'冻结名下所有账户 \n'
            fn.writelines(neirong)
        print('您已冻结你名下所有的银行卡账户！')
        return True
    elif choose == 13:
        sql = "select * from t_info  WHERE user_id = %s;" % int(args[0]['user_id'])
        print(sql)
        data = select_DB(sql)
        print('卡号        密码 用户ID 余额 状态')
        for i in data:
            print(i)
        print('------------------------------------------分割线------------------------------------------')
    elif choose == 14:
        try:
            num1 = input('输入你要转出金钱的账户：')
            num2 = input('输入你要转入金钱的账户：')
            sql1 = "select * from t_info where cardnum = %s;" % num1
            data1 = select_DB(sql1)
            sql2 = "select * from t_info where cardnum = %s;" % num2
            data2 = select_DB(sql2)
            # print(data1,data2)
            car1 = {}
            for i in data1:
                car1['cardnum'] = i[0]
                car1['balance'] = i[3]
            car2 = {}
            for i in data2:
                car2['cardnum'] = i[0]
                car2['balance'] = i[3]
        except:
            print('输入的卡号错误，或没有该卡号！')
            return False
        try:
            momey = input('请输入你要转的金额，只支持整数：')
            if int(momey) > int(car1['balance']):
                print(car1['cardnum']+'金额不足！')
            else:
                outmomey = int(car1['balance']) - int(momey)
                putmomey = int(car2['balance']) + int(momey)
                sql3 = "UPDATE t_info SET balance = %s WHERE cardnum = '%s';"  %(outmomey,car1['cardnum'])
                sql4 = "UPDATE t_info SET balance = %s WHERE cardnum = '%s';" % (putmomey, car2['cardnum'])
                print(sql3)
                print(sql4)
                update_DB(sql3)
                update_DB(sql4)
            print('转账成功！')
            with open(r'../logs/operation.log', 'a+') as fn:
                neirong = str(args[0]['username']) + '  ' + str(args[0]['user_id']) + '  ' + '账户:'+str(car1['cardnum']) +'  转出金额：'+momey+'元  到账户：'+str(car2['cardnum'])+'\n'
                fn.writelines(neirong)
            return True
        except ValueError:
            print('只能整数金额互转！')
            return False


    elif choose == 15:
        transaction(2)
        #print('提現')

