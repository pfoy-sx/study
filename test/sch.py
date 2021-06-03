#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: sch.py
@time: 2017/5/3 17:28
"""


import threading

def rwtxt():
    '''输出和输入新文本'''
    import time
    f = open('./sch.err','r')
    f.readlines()
    # f.seek(2)     # 定位到文件末尾
    while True:
        currline = f.tell()  # 获取当前位置

        time.sleep(2)
        line = f.readline().strip()  # 读入内容
        #print(line)
        if not line:         # 如果当前无信息
            f.seek(currline) # 继续定位在最末尾
        else:
            with open('new_sch.err','a+') as new:
                s = str(time.time()) + ' ' + line+'\n'
                new.writelines(s)
                print(s)      # 输出内容
        # time.sleep(2)

rw = threading.Thread(target=rwtxt,)
rw.start()