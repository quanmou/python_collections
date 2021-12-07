"""
以配置文件的方式来定义logger
"""

import logging.config


logging.config.fileConfig('./logging.conf')

rootLogger = logging.getLogger()
rootLogger.debug('This is root logger, debug message')

logger = logging.getLogger('applog')
logger.debug('This is app logger, debug message')
