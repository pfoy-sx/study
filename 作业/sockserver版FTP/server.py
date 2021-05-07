#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: server.py
@time: 2017/4/21 14:55
"""
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def setup(self):
        '''处理通讯时前要做的事情，重写父类ThreadingTCPServer的setup方法'''
        print('IP:%s Port:%s 连接进来' % (self.client_address[0],self.client_address[1]))
    def handle(self):
        '''所有跟客户端交互的都写在这里'''
        while True:
            try:
                self.setup()
            except ConnectionResetError as e:
                print('error:',e)
                break
    def finish(self):
        '''通讯完毕后处理的事情都写这里'''
        pass
if __name__ == "__main__":
    HOST, PORT = "localhost", 36969
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()