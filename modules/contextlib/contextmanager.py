"""
编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，use_with的代码可以改写如下
"""
from contextlib import contextmanager


class Query:
    def __init__(self, name):
        self.name = name

    def query(self):
        print("Query info about %s..." % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


if __name__ == "__main__":
    with create_query('Bob') as q:
        q.query()


"""
很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。
"""
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("<%s>" % name)


with tag("h1"):
    print("hello, world")
