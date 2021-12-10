"""
组件名称	对应类名	功能描述
日志器	Logger	提供了应用程序可一直使用的接口
处理器	Handler	将logger创建的日志记录发送到合适的目的输出
过滤器	Filter	提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器	Formatter	决定日志记录的最终输出格式
"""

# import logging
import logging.handlers
import datetime

logger = logging.getLogger('aa.bb.mylogger')  # 定义一个叫aa.bb.mylogger(命名是层级结构的)的日志器，不传名称则默认名称为'root'
logger.setLevel(logging.DEBUG)  # 这个级别建议设置的比后面handler的低

# 记录所有级别的日志信息到文件中
rf_handler = logging.handlers.TimedRotatingFileHandler(
    'all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")  # 定义一个格式器
rf_handler.setFormatter(rf_formatter)


# 记录error及以上日志信息到文件中
f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)  # 如果设置的比logger的级别还低是不起作用的，会按照logger的级别来过滤
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)8s - %(filename)s[:%(lineno)d] - %(message)s"))


# 输出日志到console
cons_handler = logging.StreamHandler()
cons_handler.setLevel(logging.INFO)
cons_handler.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))  # 注意s前面的-12，-8格式化方法


# 给日志器添加Handler
logger.addHandler(rf_handler)
logger.addHandler(f_handler)
logger.addHandler(cons_handler)


# 定义并关联一个过滤器
flt = logging.Filter('aa.bb')  # 日志记录只会发送给具有aa.bb命名结构的日志器
# logger.addFilter(flt)
cons_handler.addFilter(flt)  # 所有handler都可以关联这个过滤器


logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

# 用exception记录异常的栈信息
a = 'abc'
try:
    int(a)
except Exception as e:
    # logger.error(e)
    logger.exception(e)
