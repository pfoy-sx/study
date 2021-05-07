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
        conctrl = input("Choice your commodity[or input 'q' for sign out]:")
        print('-----------------------------------------')
        if conctrl == 'q':
            print('退出購物！')
            break
            #return True
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
                orderctrl = input("Choice your commodity[or input 'b' for superior menu]:")
                if orderctrl == 'b':
                    print('退出购物成功！')
                    break
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
                    ctrl = input('1:结束购物  2：继续购物  3：退出购物')
                    if ctrl == '1':
                        return orderlist,orderprice
                    elif ctrl == '2':
                        break
                    elif ctrl == '3':
                        print('欢迎下次购物!')
                        break
                    else:
                        print('Enter a mistake, please continue to enjoy shopping！')
                        break
