class Test:
    def __init__(self):
        self.__name = "scolia"

    def a(self):
        print self.__name

a = Test()
a.a()

print a.__name
print Test.__name