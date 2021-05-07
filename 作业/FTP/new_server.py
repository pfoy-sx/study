#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: new_server.py
@time: 2017/4/19 16:43
"""

import os
import hashlib
import socket

import sys
BASICS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASICS_PATH)


class Ftppath(object):
    def mkfilehome(self,user):
        self.current = os.path.abspath('.')
        self.filehome = os.path.join(self.current,user)
        if not os.path.exists(self.filehome):
            os.mkdir(self.filehome)

class Socket(Ftppath):

    def __init__(self):
        global isFlag
        isFlag = 0
        super(Socket, self).__init__()   ##继承ftppath父类
        self.sock = socket.socket()    #实例化socket对象sock
        self.sock.bind(('127.0.0.1',36969))      #绑定监听端口
        self.sock.listen(5)   #开始监听

    def verification(self,user,passwd):
        '''用户认证功能'''
        status = 1
        with open('./user','rb') as f:
            for i in f.readlines():
                if user == i.strip().decode().split(':')[0] and passwd == i.strip().decode().split(':')[1]:
                    print("认证成功")
                    status = 0
            else:
                 global isFlag
                 if status == 0:
                     isFlag = 1
                     return isFlag
                 else:
                     isFlag = 0
                     return isFlag

    def resvaccount(self):
        self.conn, self.addr = self.sock.accept()
        print("等待接受客户端认证>>>")
        user = self.conn.recv(1024)
        passwd = self.conn.recv(1024)
        print("客户端发送过来的账号：%s  密码：%s"%(user,passwd))
        isFlag = str(self.verification(user.decode(),passwd.decode()))
        self.conn.send(isFlag.encode("utf-8"))
        if int(isFlag) == 1:
            print(isFlag,type(isFlag))
            print("欢迎你登录：",user.decode())
            self.mkfilehome(user.decode())

    def status(self):
        if int(isFlag) == 0 :
            self.resvaccount()
        elif int(isFlag) == 1:
            self.connect()


    def connect(self):
        #conn,addr = self.sock.accept()    #等待client连接  conn就是client连接过来生成的一个连接实例
        print(self.addr,'连接进来了！')
        message = self.conn.recv(1024)        #接收client的数据并赋值，最多1024字节
        if not message :
            return False
        print(self.addr,"发来命令 >>：",message)
        try:
            cmd,filename = message.decode().split()
        except:
            self.conn.send(b"Commad is warning!")
        filepath = os.path.join(self.filehome,filename)
        print('文件路径：',filepath)
        if cmd == 'get':
            if os.path.isfile(filepath):
                file_size = os.stat(filepath).st_size
                self.conn.send(str(file_size).encode())  # send file size
                self.conn.recv(1024)  # 接收客户端的接收信号
                with open(filepath,'rb') as f:
                    m = hashlib.md5()
                    for line in f:
                        m.update(line)
                        self.conn.send(line)
                    print("file md5", m.hexdigest())
                    self.conn.send(m.hexdigest().encode())  # send md5
                return True
            else:
                self.conn.send(b"File is not existence!")
        elif cmd == 'put':
            print('put : %s' % filename)
            server_response = self.conn.recv(1024)  # 接收客户端发送过来的文件大小
            print("File size:", server_response)  # 打印get文件的大小
            self.conn.send(b"ready to recv file")  # 告诉server端，我现在可以开始接收了
            file_total_size = int(server_response.decode())
            file_size = 0
            getfilemd5 = hashlib.md5()
            with open(str(filepath) + '_new', 'wb') as f:
                while file_size < file_total_size:
                    if file_total_size - file_size > 1024:  # 要收不止一次
                        size = 1024
                    else:  # 最后一次了，剩多少收多少
                        size = file_total_size - file_size
                        print("The remaining data to be received:", size)
                    data = self.conn.recv(size)
                    file_size += len(data)
                    getfilemd5.update(data)
                    f.write(data)
                else:
                    new_filemd5 = getfilemd5.hexdigest()
                    print("file recv done", file_size, file_total_size)
            server_file_md5 = self.conn.recv(1024)
            print("server file md5:", server_file_md5)
            print("client file md5:", new_filemd5)
            return True
        elif cmd == 'show' and filename == 'all':
            print(self.filehome)
            fileall = str(os.listdir(self.filehome))
            print(fileall)
            self.conn.send(fileall.encode("utf-8"))
            return True
        else:
            self.conn.send(b"Commad is warning!")
            return False

    def __del__(self):
        self.sock.close()     #关闭socket连接

def main():
    s = Socket()
    while True:
        s.status()
        print('---------------------------------------')

if __name__ == '__main__':
    main()