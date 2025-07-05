import socket
import time
from loguru import logger

logger.add('log.log',format='{message}',level='DEBUG',encoding='UTF-8')
ip = input('请输入IP：\n')
ports = input('请输入端口（多个用,）隔开：\n')
print(ports.split(','))
time_start = time.time()
if ports.find(',') != -1:
    for port in ports.split(','):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            res = s.connect_ex((ip,int(port)))
            if res == 0:
                logger.debug(f'{port}端口开放')
            else:
                logger.error(f'{port}未开放')
        except Exception as e:
            logger.error(f'{port}未开放')
        s.close()
else:
    ports = int(ports)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        res = s.connect_ex((ip, ports))
        if res == 0:
            logger.debug(f'{ports}端口开放')
        s.close()
    except:
        logger.error(f'{ports}未开放')
time_end = time.time()
scan_time = time_end - time_start
logger.info(f'扫描时间：{scan_time}')