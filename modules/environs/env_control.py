"""
os.environ: 一个表示字符串环境的 mapping 对象。
例如，environ['HOME'] 是你的主目录（在某些平台上）的路径名，相当于 C 中的 getenv("HOME")。
这个映射是在第一次导入 os 模块时捕获的，通常作为 Python 启动时处理 site.py 的一部分。
除了通过直接修改 os.environ 之外，在此之后对环境所做的更改不会反映在 os.environ 中。

如果需要动态调整环境变量的值来改变代码行为，则最好采用读取文件配置的方式
"""
import os
import time
import logging
from environs import Env

env = Env()
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)


def env_test_1():
    """
    通过读取环境变量的值来改变代码行为，代码运行后无法改变环境变量值
    """
    while True:
        positive = os.environ.get("POSITIVE", "1")
        if positive == "1":
            logging.info("Positive")
        else:
            logging.info("Negative")
        time.sleep(2)


def env_test_2():
    """
    通过不断读取配置文件的方式来获取环境变量的值，从而动态改变代码行为
    """
    while True:
        env.read_env(override=True)  # 注意要添加override参数
        positive = env.bool("POSITIVE", True)
        if positive:
            logging.info("Positive")
        else:
            logging.info("Negative")
        time.sleep(2)


if __name__ == "__main__":
    # env_test_1()
    env_test_2()
