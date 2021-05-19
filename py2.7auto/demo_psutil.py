#/usr/local/env python
#coding:utf8
import psutil,datetime
#获取CPU完整信息
cputimes = psutil.cpu_times(percpu=True)
print cputimes
##获取CPU个数,logical=False不用该参数选项则默认为True，获取逻辑个数
cpucount = psutil.cpu_count(logical=False)
print cpucount
print '-----------------------------------------------------------------'
#获取内存信息
mem = psutil.virtual_memory()
print mem,mem.total,mem.free
#获取swap分区信息
memswap = psutil.swap_memory()
print memswap
print '-----------------------------------------------------------------'
#获取磁盘完整信息
diskinfo = psutil.disk_partitions()
print diskinfo
##获取分区参数使用情况，'/data'为绝对路径
diskusage = psutil.disk_usage('c://')
print diskusage
#获取总的IO个数、读写信息
diskiocount = psutil.disk_io_counters()  ##增加参数perdisk=True则获取单个分区IO个数
print diskiocount
print '-----------------------------------------------------------------'
#获取完整的网络总的IO信息，不加参数则默认pernic=False，若为True则输出每个网络接口的IOS信息
snetio = psutil.net_io_counters(pernic=True)
print snetio
print '-----------------------------------------------------------------'
#获取系统其他信息
##使用方法：psutil.users()获取当前登录系统的用户信息
nowuser = psutil.users()
print nowuser
#使用方法：psutil.boot_time()获取开机时间返回时间戳格式，可以用datetime转换为自然时间
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print '-----------------------------------------------------------------'
#列出进程ID
print psutil.pids()
#实例化一个对象，输出该pid进程的信息
p = psutil.Process(0)
#依次输出：进程名、进程bin路径、进程工作目录局对路径、进程状态、进程创建时间、进程uid信息、进行gid信息
print p.name(),p.exe(),p.cwd(),p.status(),p.create_time(),p.uids(),p.gids()
#依次输出：1）CPU时间信息包括user和system两个cpu时间、2）get进程CPU亲和度
print p.cpu_times(),p.cpu_affinity()
#依次输出：1）内存利用率，2）内存rss、vms信息
print p.memory_percent(),p.memory_info()
#依次输出：1）返回打开socket的namedutples列表；2）尽心开启的线程数
print p.io_counters(),p.num_threads()