import argparse
import threading

# 从本地模块导入目录扫描类
from dir_scan import DirScan

# 创建命令行参数解析器
parse = argparse.ArgumentParser(
    prog='信息收集工具' # 程序名称描述
)
parse.add_argument('-u','--Url',help='要收集的域名')
# required=False：不是必须的参数    action='store_true'：默认是True
parse.add_argument('-dir','--DirScan',action='store_true',required=False,help='是否扫描目录')
parse.add_argument('-foun','--FoundationInfo',action='store_true',required=False,help='是否收集基础信息')
parse.add_argument('-dict','--dirdict',required=False,help='目录字典')
args = parse.parse_args()
print(args.DirScan)
print(args.URL)
print(args.FoundationInfo)

# if args.DirScan:
#     if args.dirdict is False:
#         print('需要设置字典')
#     dirscan = DirScan()
#     th = threading.Thread(target=dirscan.run,args=[args.url,args.dirdict]).start()