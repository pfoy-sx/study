#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/13 17:15
# @Author  : Beam
# @Site    : 
# @File    : rwfile.py
# @Software: PyCharm

import json

result = []

#查出URL对应的backend位置，把该URL下的配置加入到result列表里
def seach(url):
    #检查有没有指定backend，True返回一个列表，False返回为空
    with open('ha.conf','r',encoding='utf-8') as fn:
        flag = False
        for line in fn:
            if line.strip().startswith('backend') and line.strip() == "backend " + url:
                flag = True
                continue
            if flag and  line.strip().startswith('backend'):
                flag = False
                break
            if flag and line.strip():    #空字符串是假的
                result.append(line.strip())
    return result

def add(backend,record):
    result_list = seach(backend)
    if not result_list:
        with open('ha.conf','r') as old,open('new_ha.conf','w') as new:
            for line in old:
                new.write(line)
            new.write('\nbackend ' + backend + '\n')
            new.write(' '*8 + record + '\n')
    else:
        #若ha.conf配置文件有这个backend以及rd内容直接复制一份配置文件
        if record in result_list:
            with open('ha.conf','r') as old,open('new_ha.conf','w') as new:
                for line in old:
                    new.write(line)
        else:
            #若ha.conf配置文件有这个backend，另外没有rd内容直接在该backend模块下增加rd内容
            result_list.append(record)
            with open('ha.conf','r') as old,open('new_ha.conf','w') as new:
                flag = False
                for line in old:
                    if line.strip().startswith('backend') and line.strip() == "backend " + backend:
                        flag = True
                        new.write(line)
                        for i in result_list:
                            new.write(' '*8 + i + '\n')
                        continue
                    if flag and line.strip().startswith('backend'):
                        flag = False
                        new.write(line)
                        continue
                    if line.strip() and not flag:
                        new.write(line)

bk = 'aa.example.com'
rd = 'server 172.27.0.44 172.27.0.44 weight 20 maxconn 3000'
add(bk,rd)


