from loguru import logger

logger.add('file_{time}.log',format="{time}{name}{level}{message}",level='DEBUG',rotation='5 MB',encoding='utf-8')

# logger.debug('debug日志')
# logger.info('info日志')
# logger.warning('warning日志')
# logger.error('error日志')
# logger.critical('critical日志')

for _ in range(0,10):
    if _%2 == 0:
        logger.info(f'{_}是2的倍数')

