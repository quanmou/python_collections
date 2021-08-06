# -*- coding:utf-8 -*-


# python2, python3度可以使用的方法
class A(object):
    def __init__(self, x):
        self.x = x


# 方法1
class B(A):
    def __init__(self, x, y):
        A.__init__(self, x)
        self.y = y


# 方法2
class C(A):
    def __init__(self, x, y):
        super(C, self).__init__(x)
        # super(__class__, self).__init__(x)  # python3，可以直接使用__class__拿到类名
        # super().__init__(x)  # python3，super中的参数可以省略
        self.y = y


if __name__ == "__main__":
    b = B("foo", "bar")
    c = C("foo", "bar")
    print(b.x, b.y)
    print(c.x, c.y)
