#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: socketServer.py
@time: 2017/4/20 20:25
"""


import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        while True:
            try:
              # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
              # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print('error:',e)
                break
if __name__ == "__main__":
    HOST, PORT = "localhost", 36969
    # Create the server, binding to localhost on port 9999
    server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()