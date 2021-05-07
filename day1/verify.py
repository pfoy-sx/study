#coding:utf8
#验证用户，三次失败锁定用户

import sys
dic = {}
with open('./user.txt') as line:
    for fd in line:
        if fd.startswith('user'):
            dic['user'] = fd.split(':')[-1].strip()
        if fd.startswith('passwd'):
            dic['passwd'] = fd.split(':')[-1].strip()
        if fd.startswith('status'):
            dic['status'] = fd.split(':')[-1].strip()
if int(dic['status']) == 1:
    print('用户%s已被锁定,请联系管理员。' %dic['user'])
    sys.exit(1)
else:
    count = 0
    while count < 3:
        iuser = input('Please input your username:')
        ipwd = input('Enter password for user: ')
        if dic['user'] == iuser and dic['passwd'] == ipwd:
            print('通过验证')
            sys.exit(1)
        else:
            print('验证失败，请重新验证！')
            count +=1
        if count == 3:
            print('验证三次失败，账户已锁定！')
            dic['status'] = '1'
            with open('./user.txt','w') as fd:
                for i in dic:
                    oput = str(i)+':'+dic[i]+'\n'
                    fd.write(oput)
