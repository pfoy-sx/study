#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: stu_paramiko.py
@time: 2017/4/24 9:30
"""
import time

import paramiko
'''以下部分是paramiko模拟ssh连接客户端执行命令部分'''
private_key = paramiko.RSAKey.from_private_key_file('C:/Users/Lenovo/.ssh/id_rsa')    #设置发起连接server的密钥文件路径
ssh = paramiko.SSHClient()  #实例化ssh对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #允许连接不在know_hosts文件中的主机
ssh.connect('104.168.87.81',port=22,username='root',pkey=private_key)   #连接服务器  ,这个pkey就是上面定义的private_key
commd = input('>>')   #输入命令
stdin,stdout,stderr = ssh.exec_command(commd)  #执行命令，会有3个返回，stdin是你输入的命令，stdout是正确输出，stderr是错误输出
result = stdout.read()   #stdout,stderr只有其中一个会有结果
print(result.decode())
time.sleep(10)
ssh.close()


###

# import paramiko
# '''以下是paramiko模拟xftp传输部分'''
# transport = paramiko.Transport(('192.168.0.242',22))
# transport.connect(username='Beam',password='oracle')
# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.put('/tmp/test.txt','/tmp/')
# transport.close()