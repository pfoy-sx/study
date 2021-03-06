#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: ssh_s.py
@time: 2017/4/17 16:32
"""

import socket, os, time

server = socket.socket()
server.bind(('localhost', 9999))

server.listen()

while True:
    conn, addr = server.accept()
    print("new conn:", addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令:", data.decode())
        cmd_res = os.popen(data.decode()).read()  # 接受字符串，执行结果也是字符串
        print("before send", len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."

        conn.send(str(len(cmd_res.encode())).encode("utf-8"))  # 先发大小给客户端
        time.sleep(0.5)
        conn.send(cmd_res.encode("utf-8"))
        print("send done")

server.close()