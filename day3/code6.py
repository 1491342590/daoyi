import psutil

# #几核
# print(psutil.cpu_count())
#
# #物理核心
# print(psutil.cpu_count(logical=False))
#
# # cpu运行时间
# print(psutil.cpu_times())
#
# # CPU的使用率
# print(psutil.cpu_percent(interval=1,percpu=True))
#
# # 物理内存
# print(psutil.virtual_memory())
#
# # 交换内存
# print(psutil.swap_memory())
#
# # 磁盘分区、使用信息
# print(psutil.disk_partitions())
# print(psutil.disk_usage('C:\\'))
#
# # 磁盘io信息
# print(psutil.disk_io_counters())
#
# # 网络信息
# print(psutil.net_io_counters())


# 网络接口信息
print(psutil.net_if_addrs())

# 当前网络连接信息
print(psutil.net_connections())

# 进程id,进程详细信息，
print(psutil.pids())
print(psutil.Process(4))

p = psutil.Process(4)
print(p.exe())