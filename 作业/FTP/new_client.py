#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: new_client.py
@time: 2017/4/19 16:43
"""

import os
import hashlib
import socket

import sys
BASICS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASICS_PATH)

class Socket(object):
    def __init__(self):
        self.isFlag = 0
        self.c = socket.socket()
        self.c.connect(('localhost', 36969))

    def __help(self):
        print("""Commad warning:
            get filename
            put filename
            show all
        """)


    def login(self):
        while True:
            user = input("user: >>")
            passwd = input("passwd:>>")
            self.c.send(user.encode("utf-8"))
            self.c.send(passwd.encode("utf-8"))
            self.isFlag = int(self.c.recv(1024).decode())
            print("认证结果：",self.isFlag)
            if self.isFlag == 1:
                print("认证成功！")
                break
            else:
                print("认证失败！")
                continue




    def status(self):
        if int(self.isFlag) == 0 :
            self.login()
        elif int(self.isFlag) == 1:
            self.connect()

    def connect(self):
        try:
            while True:
                message = input(">>:").strip()
                if not message:
                    continue
                #try:
                cmd,filename = message.split()
                if cmd == 'get':
                    print(filename)
                    self.c.send(message.encode('utf-8'))
                    server_response = self.c.recv(1024)    #服务器端返回文件的大小
                    print("File size:",server_response)  #打印get文件的大小
                    self.c.send(b"ready to recv file")   #告诉server端，我现在可以开始接收了
                    file_total_size = int(server_response.decode())
                    file_size = 0
                    getfilemd5 = hashlib.md5()
                    with open(str(filename)+'_new','wb') as f:
                        while file_size < file_total_size:
                            if file_total_size - file_size > 1024:  # 要收不止一次
                                size = 1024
                            else:  # 最后一次了，剩多少收多少
                                size = file_total_size - file_size
                                print("The remaining data to be received:", size)
                            data = self.c.recv(size)
                            file_size += len(data)
                            getfilemd5.update(data)
                            f.write(data)
                        else:
                            new_filemd5 = getfilemd5.hexdigest()
                            print("file recv done", file_size, file_total_size)
                    server_file_md5 = self.c.recv(1024)
                    print("server file md5:", server_file_md5)
                    print("client file md5:", new_filemd5)
                    return True
                elif cmd == 'put':
                    self.c.send(message.encode("utf-8"))
                    if os.path.isfile(filename):
                        file_size = os.stat(filename).st_size
                        print(file_size)
                        self.c.send(str(file_size).encode("utf-8"))  # send file size
                        self.c.recv(1024)  # 接收客户端的接收信号
                        with open(filename, 'rb') as f:
                            m = hashlib.md5()
                            for line in f:
                                m.update(line)
                                self.c.send(line)
                            print("file md5", m.hexdigest())
                            self.c.send(m.hexdigest().encode())  # send md5
                            return True
                    else:
                        self.c.send(b"File is not existence!")
                elif cmd == 'show':
                    self.c.send(message.encode('utf-8'))
                    data = self.c.recv(1024).decode()
                    print(data)
                else:
                    self.__help()
                # except:
                #     print('Commad is warning!')
                #     continue
        except:
            self.__help()

    def __del__(self):
        self.c.close()

def main():
    c = Socket()
    while True:
        c.status()
        print('---------------------分割线------------------')


if __name__ == '__main__':
    main()