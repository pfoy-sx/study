#coding:utf8
from IPy import IP

#区分该地址是IPV4还是IPV6
version = IP('192.168.10.0/8').version()
print version
#指定网段IP地址并输出
ip = IP('192.168.10.0/8')

