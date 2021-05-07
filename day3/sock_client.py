#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: sock_client.py
@time: 2017/4/14 9:53
"""

import socket
def main():
    cli_sock = socket.socket()
    cli_sock.connect(('localhost',36969))   #连接server端，端口要跟server端监听的端口一致
    cli_sock.send(b'beam')
    data = cli_sock.recv(1024)
    print("Server receve:",data)
if __name__ == '__main__':
    main()