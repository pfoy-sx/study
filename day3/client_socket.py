#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: client_socket.py
@time: 2017/4/15 14:59
"""

import socket
def main():
    cli_sock = socket.socket()
    cli_sock.connect(('localhost',36969))   #连接server端，端口要跟server端监听的端口一致
    while True:
        message = input(">>:")
        if not message:
            continue
        cli_sock.send(message.encode('utf-8'))
        data = cli_sock.recv(1024)
        print("Server receve:",data)
if __name__ == '__main__':
    main()

