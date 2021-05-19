#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/14 10:39
# @Author  : Beam
# @Site    : 
# @File    : demo_difflib.py
# @Software: PyCharm

import difflib,sys

try:
    textfile1 = 'D:/Python/pythonauto/demo_urllib1.py' #sys.argv[1]
    textfile2 = 'D:/Python/pythonauto/demo_urllib2.py' #sys.argv[2]
except Exception,e:
    print "Error :" + str(e)
    print "Usage:python %s filename1 filename2" %sys.argv[0]

def readFile(filename):    #文件读取分隔函数
    try:
        with open(filename,'rb') as filehandle:
            text = filehandle.read().splitlines()   #读取后以行的形式进行分隔
            return text
    except IOError as error:
        print 'Read file Error:' + str(error)
        sys.exit()

if textfile1 == '' or textfile2 == '':
    print "Usage:python %s filename1 filename2" %sys.argv[0]
    sys.exit()

text_lines1 = readFile(textfile1)
text_lines2 = readFile(textfile2)

d = difflib.HtmlDiff()
con = d.make_file(text_lines1,text_lines2)
print con
