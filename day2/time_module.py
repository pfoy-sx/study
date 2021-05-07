import time
# print(time.altzone)                  #返回当前时区与格林时区的时间差，以秒为计算单位 -32400
# print(time.asctime())                #返回的时间格式Fri Jan 20 11:26:51 2017
# t = time.localtime()                 #返回本地时间struct time格式：time.struct_time(tm_year=2017, tm_mon=1, tm_mday=20, tm_hour=14, tm_min=52, tm_sec=14, tm_wday=4, tm_yday=20, tm_isdst=0)
# print(t.tm_year,t.tm_yday)           #打印t这个对象的年和日2017 20,是一个字符串类型
# print(time.asctime(time.localtime()))#返回时间格式Fri Jan 20 14:54:26 2017
# print(time.ctime())                  #返回时间格式Fri Jan 20 14:57:24 2017
#
# #日期字符串转成时间戳
# struct = time.strptime("2017/01/20 15:55","%Y/%m/%d %H:%M")   #日期字符串转成struct时间对象格式，/和：都是一一对应的
# print(struct)                        #返回结果time.struct_time(tm_year=2017, tm_mon=1, tm_mday=20, tm_hour=15, tm_min=55, tm_sec=0, tm_wday=4, tm_yday=20, tm_isdst=-1)
# stamp = time.mktime(struct)          #把struct格式转换成时间戳
# print(stamp)                         #返回1484898900.0
#
# #将时间戳转换为字符串格式
# t = time.time()                      #返回当前时间的时间戳
# print(time.gmtime(t+28800))          #把时间戳转换为struct格式,格林地区的时间比中国本地的时区慢8小时
# print(time.strftime("%Y-%m-%d %H:%M",time.gmtime(t+28800)))    #把struct格式转换为指定的日期格式2017-01-20 17:21

#
# import time
# import datetime
#
# print(datetime.datetime.now())                                  #返回当前完整时间 2017-01-20 17:52:12.479214
# print(datetime.date.fromtimestamp(time.time()))                 #把时间戳直接返回年月日2017-01-20
# print(datetime.datetime.now() + datetime.timedelta(+2))         #当前时间加2天    2017-01-22 17:52:12.479214
# print(datetime.datetime.now() + datetime.timedelta(-6))         #当前时间减6天    2017-01-14 17:52:12.479214
# print(datetime.datetime.now() + datetime.timedelta(hours=-3))   #当前时间减3小时  2017-01-20 14:52:12.479214
# print(datetime.datetime.now() + datetime.timedelta(minutes=5))  #当前时间加5分钟   2017-01-20 17:57:12.479214
# now = datetime.datetime.now()                                   #获取当前完整时间
# print(now.replace(year=1992,month=7,day=26))                    #直接把年月日的时间更替换指定的年月日，时分秒也可以替换




