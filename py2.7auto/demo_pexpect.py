#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/31 10:54
# @Author  : Beam
# @Site    : 
# @File    : demo_pexpect.py
# @Software: PyCharm

import pexpect

child = pexpect.spawn('scp foo root@114.55.86.245')   #spawn启动奢侈品程序
child.expect('Password:')
child.sendline('dev.app@xuehu365*for@2016')