#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : ${DATE} ${TIME}
# @Author  : Beam

import multiprocessing
import time,threading

def thread_run():
    print(threading.get_ident())  ##get_ident()获取该线程的线程号
def run(name):
    time.sleep(2)
    print('Hello',name)
    t = threading.Thread(target=thread_run,)
    t.start()
if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=("Process %s" %i,))
        p.start()

