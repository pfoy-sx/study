#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: 红绿灯示例.py
@time: 2017/4/28 9:50
"""


import time
import threading

event = threading.Event()  #实例化一个事件

def lighter():
    count = 0
    event.set()  #设置一个标记位，set()代表可以通行
    while True:  #循环红绿灯状态
        if count > 5 and count < 10:   #假设6-9秒是红灯
            event.clear()  #把标记位清空，代表不能通行
            print("\033[41;1mRed light is on .....\033[0m")
        elif count > 10 :  #假设第10秒后变红灯，count并变回0
            event.set()
            count = 0
        else:
            print("\033[42;1mGreen light is on .....\033[0m")
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():  #is_set()判断其它线程有没有设置标记
            print("%s Runging ...." % name)
            time.sleep(1)
        else:
            print("Light is Red , %s is waitting ...." % name)
            event.wait()   #等待，因为另外一个线程把标记位清掉了，所以这里可以wait()等待新的标记位
            print("\033[34;1mGreen light is on ,start going .....\033[0m")


light = threading.Thread(target=lighter,)
light.start()
car1 = threading.Thread(target=car,args=("Tesla one",))
car1.start()
# car2 = threading.Thread(target=car,args=("Tesla two",))
# car2.start()
