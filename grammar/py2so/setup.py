"""
需要先安装cython， linux需要安装python-devel, gcc
调用python setup.py build_ext，会在同级目录下多一个hello.c文件，并生成一个build目录，里面有打包好的so文件
"""
from distutils.core import setup
from Cython.Build import cythonize


setup(ext_modules=cythonize(["hello.py"]))
# setup(ext_modules=cythonize(["hello1.py", "hello2.py", "hello3.py"]))  # 同时打包多个py文件
