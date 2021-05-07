#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: server_socket.py
@time: 2017/4/15 11:07
"""

import socket

class Socket(object):

    def __init__(self):
        self.sock = socket.socket()    #实例化socket对象sock
        self.sock.bind(('127.0.0.1',36969))      #绑定监听端口
        self.sock.listen()   #开始监听

    def connect(self):
        self.conn,self.addr = self.sock.accept()    #等待client连接  conn就是client连接过来生成的一个连接实例
        self.message = self.conn.recv(1024)       #接收client的数据并赋值，最多1024字节
        if not self.message :
            return False
        print(self.addr,"发来命令 >>：",self.message)

        self.conn.send(self.message)      #返回结果到client端

    def __del__(self):
        self.sock.close()     #关闭socket连接

def main():
    s = Socket()
    while True:
        s.connect()

if __name__ == '__main__':
    main()