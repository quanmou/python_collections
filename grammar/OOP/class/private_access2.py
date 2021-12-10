class Test:
    def __init__(self):
        self.name = "public"
        self.__name = "scolia"

    def a(self):
        print(self.__name)


a = Test()
a.a()

print(a.name)
print(Test.name)
print(a.__name)
print(Test.__name)
