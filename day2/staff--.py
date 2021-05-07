#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/20 14:07
# @Author  : Beam


"""
员工信息表程序，实现增删改查操作：

可进行模糊查询，语法至少支持下面3种:
　　select name,age from staff_table where age > 22
　　select  * from staff_table where dept = "IT"
    select  * from staff_table where enroll_date like "2013"
查到的信息，打印后，最后面还要显示查到的条数
可创建新员工纪录，以phone做唯一键，staff_id需自增
可删除指定员工信息纪录，输入员工id，即可删除
可修改员工信息，语法如下:
　　UPDATE staff_table SET dept="Market" where dept = "IT"
 注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码
"""


import re
import shutil

rows = ["staff_id", "name", "age", "phone", "dept", "enroll_date"]
OPTCRUXS = ['from t_staff where','age > 22','dept = "IT"','enroll_date like "2013"']
FIELD = ['staff_id','phone','name','age','dept','staff','enroll_date','*']

# def __init__():
#     """[1:{},2:{},3:{} ....]"""
#     infolists = []
#     infodict = {}
#     with open(r'./staff.txt','r') as fn:
#         for i in fn.readlines():
#             try:
#                 INFODICT = {}
#                 INFODICT['staff_id'] = i.strip().split(',')[0]
#                 INFODICT['phone'] = i.strip().split(',')[1]
#                 INFODICT['name'] = i.strip().split(',')[2]
#                 INFODICT['age'] = i.strip().split(',')[3]
#                 INFODICT['dept'] = i.strip().split(',')[4]
#                 INFODICT['staff'] = i.strip().split(',')[5]
#                 INFODICT['enroll_date'] = i.strip().split(',')[6]
#                 infodict[i.strip().split(',')[0]] = INFODICT
#                 infolists.append(i.strip().split(',')[0])
#             except IndexError:
#                 continue
#     return infolists,infodict

#判断select语法
def seljudge(sql):
    import re
    temps = re.search('select (.*)(from t_staff where)(.*)', sql).group(1).strip()
    optcrux = re.search('select (.*)(from t_staff where)(.*)', sql).group(2).strip()
    condition = re.search('(.*)(from t_staff where)(.*)', sql).group(3).strip()
    lis = temps.strip().split(',')
    for i in lis:
        if i not in FIELD:
            return False
    if optcrux not in OPTCRUXS or condition not in OPTCRUXS:
        return False
    return lis,condition

def select(sql):
    n = 0
    if seljudge(sql):
        all_info = []
        search_list = sql.strip().split(' ')
        with open(r'./staff.txt', 'r') as f:
            for line in f:
                user_info = line.strip().split(',')
                if search_list[1] == '*':
                    if 'where' not in search_list:
                        conditional = str(user_info).replace(',', ' ')
                        print(conditional)
                        n += 1
                    elif search_list[5] in rows and search_list[6] == '=':
                        if eval(search_list[7]) in user_info or search_list[7] in user_info:
                            print(user_info)
                            n += 1
                    elif search_list[5] in rows and search_list[6] == 'like':
                        for every in user_info:
                            if eval(search_list[7]) in every:
                                print(user_info)
                                n += 1
                else:
                    found_info = []
                    if search_list[1].split(',')[0] == 'name' and search_list[1].split(',')[1] == 'age':
                        if search_list[6] == '=' and search_list[7] in user_info[2]:
                            found_info.append([user_info[1], user_info[2]])
                            print(found_info)
                            n += 1
                        elif search_list[6] == '>' and search_list[7] < user_info[2]:
                            found_info.append([user_info[1], user_info[2]])
                            print(found_info)
                            n += 1
                    else:
                        print("当前条件查询无结果")
                        break
        print("select结果共%s条"% n)
    else:
        print('select语法错误！')

def insert(sql):
    add_list = sql.split(',')
    phone = []
    with open(r'./staff.txt', 'r+') as f:
        user_id = 0
        for line in f:
            user_info = line.strip().split(',')
            if user_info:
                phone.append(user_info[3])
            if user_info[0].isdigit() and user_id < int(user_info[0]):
                user_id = int(user_info[0])
        if add_list[2] not in phone:
            value = re.search('(values)(.*)',sql).group(2).strip().replace("'",'').replace('(','').replace(')','')
            f.write('%s,%s\n'%(str(user_id+1),value))
            print('手机号为%s员工信息已经添加成功' % add_list[2])
        else:
            print("输入的员工信息已存在\n")

def update(sql):
    mod_list = sql.strip()  # .split(' ')
    old_dept = re.search('where(.*)', mod_list).group(1).strip().split(' ')[2].replace('"', ' ').strip()
    new_dept = re.search('set(.*)where', mod_list).group(1).strip().split(' ')[2].replace('"', ' ').strip()
    with open(r'./staff.txt', 'r', encoding='utf-8') as old, open(r'./staff.txt.new', 'w', encoding='utf-8') as new:
        for line in old:
            user_info = line.strip().split(',')
            if user_info and user_info[4] == old_dept:
                user_info[4] = new_dept
                new_info = ','.join(user_info)
                new.write('%s\n' % new_info)
            else:
                new.write('%s\n' % line.strip())
        print('更新成功')
    shutil.copy('./staff.txt.new', './staff.txt')

def delete(sql):
    staff_id = re.search('(=)(.*)',sql).group(2).strip()
    if not staff_id.isdigit():
        print("输入错误")
        return
    else:
        with open(r'./staff.txt', 'r', encoding='utf-8') as old, open(r'./staff.txt.new', 'w', encoding='utf-8') as new:
            for line in old:
                user_info = line.strip().split(',')
                if staff_id == user_info[0]:
                    print("该员工ID删除成功")
                    continue
                elif not user_info[0].isdigit():
                    new.write(line.strip())
                else:
                    new.write('%s\n' % line.strip())
        shutil.copy('./staff.txt.new', './staff.txt')




if __name__ == '__main__':
    print('#Sql Example：select name,age from t_staff where age > 22  (!!!tablename:t_staff!!!)')
    print("insert: insert into t_staff  values ('Beam',25,'13956987452','IT','2016-08-08')")
    print('update: update t_staff set dept = "Sales"  where dept = "IT"')
    print('delete: delete from staff_table where staff_id = 3')

    while True:
        sql = input('请输入sql语句：').strip()
        if sql.lower() == 'q':
            exit('退出')
        if sql.lower().startswith('select'):
            select(sql)
            continue
        if sql.lower().startswith('insert'):
            #insert into t_staff  values ('Beam',25,'13956987452','IT','2016-08-08')
            insert(sql)
            continue
        if sql.lower().startswith('update'):
            update(sql)
            continue
        if sql.lower().startswith('delete'):
            delete(sql)
            continue
        else:     #第一次语法判断
            print('输入错误，重新输入')