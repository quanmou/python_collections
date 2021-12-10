import logging


# 使用配置
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

# 换一种方式
# logging.log(logging.DEBUG, "This is a debug log.")
# logging.log(logging.INFO, "This is a info log.")
# logging.log(logging.WARNING, "This is a warning log.")
# logging.log(logging.ERROR, "This is a error log.")
# logging.log(logging.CRITICAL, "This is a critical log.")

# 写到文件
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename='my.log', 'filemode'='a', level=logging.DEBUG, format=LOG_FORMAT)
#
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")


# 指定时间格式
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
#
# logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
#
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")


# 加入其它信息
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s[%(ip)s] - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.warning("Some one delete the log file.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})
