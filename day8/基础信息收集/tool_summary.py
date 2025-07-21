import argparse
import threading

# 从本地模块导入目录扫描类
from dir_scan import DirScan

# 创建命令行参数解析器
parse = argparse.ArgumentParser(
    prog='信息收集工具' # 程序名称描述
)
parse.add_argument('-u','--Url',help='要收集的url')
# required=False：表明不是必须的参数    action='store_true'：开关--默认是False
parse.add_argument('-dir','--DirScan',action='store_true',required=False,help='是否扫描目录')
parse.add_argument('-foun','--FoundationInfo',action='store_true',required=False,help='是否收集基础信息')
parse.add_argument('-dict','--DirDict',required=False,help='目录字典')
# 解析用户在命令行中输入的参数，并将它们存储在 args 对象中。
args = parse.parse_args()
# print(args.DirScan)
# print(args.Url)
# print(args.FoundationInfo)

if args.DirScan:
    # 目录字典是否设置
    if args.DirDict is False:
        print('需要设置字典')
    # 创建 DirScan 类的一个实例
    dirscan = DirScan()
    # 创建一个新的线程 (th)。线程的目标函数是 dirscan 对象的 run 方法，
    # args.Url和 args.dirdict 作为参数传递给 run 方法。
    th = threading.Thread(target=dirscan.run,args=[args.Url,args.DirDict]).start()
