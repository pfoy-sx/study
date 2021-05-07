#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: sock_server.py
@time: 2017/4/14 9:53
"""

import socket

def main():
    sock = socket.socket()    #实例化socket对象sock
    sock.bind(('localhost',36969))      #绑定监听端口
    sock.listen()   #开始监听
    conn,addr = sock.accept()    #等待client连接  conn就是client连接过来生成的一个连接实例
    data = conn.recv(1024)       #接收client的数据并赋值，最多1024字节
    conn.send(data.upper())      #返回结果到client端，把它发过来的东西变成大写返回

    sock.close()     #关闭socket连接

if __name__ == '__main__':
    main()