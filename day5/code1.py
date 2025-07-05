import argparse
import time

parser = argparse.ArgumentParser(
    prog='账号密码爆破工具',
    description='RDP、SSH、FTP服务账号密码爆破工具',
    epilog='版权信息'
)
parser.add_argument('-u', '--user', help='用户名字典路径', required=True)
parser.add_argument('-p', '--password', help='密码字典路径', required=True)
parser.add_argument('-host', '--hostaddress', help='主机地址', required=True)
parser.add_argument('-t', '--thread', help='多线程', action='store_true')
args = parser.parse_args()
print(f'用户名字典路径{args.user}')
print(f'密码字典路径{args.password}')
print(f'主机地址{args.hostaddress}')
print(f'多线程{args.thread}')