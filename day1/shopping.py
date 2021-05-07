#coding:utf8
#购物车：
#1. 商品信息- 数量、单价、名称
#2. 用户信息- 帐号、密码、余额
#3. 用户可充值
#4. 购物历史信息
#5. 允许用户多次购买，每次可购买多件
#6. 余额不足时进行提醒
#7. 用户退出时 ，输出当次购物信息
#8. 用户下次登陆时可查看购物历史
#9. 商品列表分级显示
#三级目录退出


import sys,os,operator
##定义商品列表
goodList = {
    "家用电器":{"洗衣机":"1500","电视":"3000","冰箱":"1312","吸油烟机":"1400",},
    "手机数码":{"笔记本电脑":"5555","手机":"2999","蓝牙耳机":"300","数码相机":"6666",},
    "男装女装":{"西服":"3000","衬衫":"299","连衣裙":"888","超短裙":"666",},
    "酒水饮料":{"啤酒":"25","白酒":"333","红酒":"999","可乐":"3",},
}

#初始化数据
def _init():
    if not os.path.exists('./Userlist.txt'):
        #os.mknod('./Userlist.txt')
        dic = {'user':'beam','passwd':'123456','balance':'10.99','order':'None'}
        with open('./Userlist.txt','w') as fd:
            for key in dic:
                data = str(key)+':'+dic[key]+'\n'
                fd.write(data)

#获取个人信息
def getInfo():
    dic = {}
    with open('./Userlist.txt') as line:
        for fd in line:
            if fd.startswith('user'):
                dic['user'] = fd.split(':')[-1].strip()
            if fd.startswith('passwd'):
                dic['passwd'] = fd.split(':')[-1].strip()
            if fd.startswith('balance'):
                dic['balance'] = fd.split(':')[-1].strip()
            if fd.startswith('order'):
                dic['order'] = fd.split(':')[-1].strip()
    return dic

def login(dic):
    iuser = input('Please input your username:')
    ipwd = input('Enter password for user: ')
    if dic['user'] == iuser and dic['passwd'] == ipwd:
        return True
    else:
        return False

def outinfo(data):
    data = data
    print('欢迎您：' + data['user'] +'，'+'您的余额：'+data['balance']+','+'历史购物清单'+data['order'])

#购买商品方法
def buyList():
    ##存放菜单目录
    saveshoplist = []
    #存放购买商品的列表
    orderlist = []
    #存放商品的价格
    savepicelist = []
    #订单价格
    orderprice = []
    while True:
        print('---------------------商品列表---------------------')
        for key1,value1 in enumerate(goodList):
            print(key1,value1)
            saveshoplist.append(value1)
        conctrl = input("Please enter the serial number to select the corresponding type of goods[or input 'q' for sign out]:")
        print('-----------------------------------------')
        if conctrl == 'q':
            print('再见！')
            sys.exit(1)
        elif not (conctrl == '0' or conctrl == '1' or conctrl == '2' or conctrl == '3'):
            print('输入有误，请重新输入')
            print('-----------------------------------------')
        else:
            while True:
                ordershop = []
                savepicelist.clear()
                for key2,value2 in enumerate(goodList[saveshoplist[int(conctrl)]]):
                    shopprice = goodList[saveshoplist[int(conctrl)]][value2]
                    print('\t',key2,value2,shopprice)
                    ordershop.append(value2)
                    savepicelist.append(shopprice)
                #print(savepicelist)
                #print(ordershop)
                orderctrl = input("Choice your commodity[or input 'q' for sign out]:")
                if orderctrl == 'q':
                    print('再见！')
                    sys.exit(1)
                elif not (orderctrl == '0' or orderctrl == '1' or orderctrl == '2' or orderctrl == '3'):
                    print('输入有误，请重新输入')
                    print('-----------------------------------------')
                else:
                    count = input('Input your commodity count:')
                    pass##输入数量有错误则进行操作
                    orderlist.append(ordershop[int(orderctrl)])
                    orderprice.append(int(savepicelist[int(orderctrl)])*int(count))
                    #print(orderlist)
                    #print(orderprice)
                    ctrl = input('Input 1 to Settlement;2 to continue shopping;3 to return to superior product;4 to Exit system:')
                    if ctrl == '1':
                        return orderlist,orderprice
                    elif ctrl == '2':
                        continue
                    elif ctrl == '3':
                        break
                    elif ctrl == '4':
                        sys.exit(1)
                    else:
                        print('Enter a mistake, please continue to enjoy shopping！')
                        continue
##算商品的总额
def settlementMom(orderprice):
    momeny = 0
    for i in orderprice:
        momeny+= float(i)
    return momeny

##充值
def rechargeMom(s):
    k = input('Input your recharge momeny:')
    balance = float(s) + float(k)
    return balance

#购物结算
def payMomeny(s,mustpay):
    balance = float(s) - mustpay
    if operator.lt(balance,mustpay) :
        case = input('Your balance is not enough, do you go to the top?[y or n]')
        print('-----------------------------------------')
        if case == 'y':
            newbalance = float('%0.3f'%rechargeMom(balance))
            return newbalance
        elif case == 'n':
            print('End shopping！')
            sys.exit(1)
        else:
            print('Input warnning!Please re shopping!')
            sys.exit(1)
    elif balance>=0:
        return balance
    else:
        print('遇到不知名错误退出')
        sys.exit(2)

def writeInfo(data,balance,orderlist):
    data['balance'] = balance
    data['order'] = orderlist
    #print(data)
    print("本次购物清单：%s，余额：%s" % (orderlist,balance))
    with open('./Userlist.txt','w') as fd:
        for key in data:
            winfo = str(key)+':'+str(data[key])+'\n'
            fd.write(winfo)

#主函数
def main():
    _init()
    data = getInfo()
    ##登陆模块
    if login(data):
        print('通过验证')
        outinfo(data)
    else:
        print('验证失败，请重新验证！(再次错误直接退出)')
        login(data)
    orderlist,orderprice = buyList()
    mustpay = settlementMom(orderprice)
    balance = payMomeny(data['balance'],mustpay)
    writeInfo(data,float(balance),orderlist)
    print('欢迎下次购物！')

if __name__ == '__main__':
    main()