"""
使用包含配置信息的dict实现日志配置
Python 3.2中引入的一种新的配置日志记录的方法--用字典来保存logging配置信息。
这相对于上面所讲的基于配置文件来保存logging配置信息的方式来说，功能更加强大，也更加灵活，因为我们可把很多的数据转换成字典。
比如，我们可以使用JSON格式的配置文件、YAML格式的配置文件，然后将它们填充到一个配置字典中；
或者，我们也可以用Python代码构建这个配置字典，或者通过socket接收pickled序列化后的配置信息。
总之，你可以使用你的应用程序可以操作的任何方法来构建这个配置字典。
"""

import logging.config
import yaml


class NoConsoleFilter(logging.Filter):
    def filter(self, record):
        return not (record.levelname == 'INFO') & ('no-console' in record.msg)


# 使用yaml格式的配置文件
# with open('./logging.yaml', 'r') as f:
#     dict_conf = yaml.load(f)

# 直接使用python dict
dict_conf = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)-8s - %(message)s"
        }
    },
    "filters": {
        "no_console_filter": {
            "()": "__main__.NoConsoleFilter"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filters": [
                "no_console_filter"
            ],
            "stream": "ext://sys.stdout"
        },
        "console_err": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "filename": "test.log",
            "formatter": "simple",
            "maxBytes": 1024,
            "backupCount": 3
        }
    },
    "loggers": {
        "simpleExample": {
            "level": "DEBUG",
            "handlers": [
                "console"
            ],
            "propagate": True
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console_err"
        ]
    }
}

logging.config.dictConfig(dict_conf)
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('no-console. Should not be in console, but be in test.log!')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')