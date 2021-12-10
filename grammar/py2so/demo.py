"""
测试打包是否成功
将build里的so文件移到同级目录下，将hell.py删除掉
运行python demo.py输出"hello Tom"，说明调用的是so文件里的greet
"""

from hello import greet
print(greet("Tom"))
