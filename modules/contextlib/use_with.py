"""
任何对象，只要正确实现了上下文管理，就可以用于with语句。
"""


class Query:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Begin")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Error")
        else:
            print("End")

    def query(self):
        print("Query info about %s..." % self.name)


if __name__ == "__main__":
    with Query('Bob') as q:
        q.query()
