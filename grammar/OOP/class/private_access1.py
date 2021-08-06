class Test:
    __name = "scolia"

    def a(self):
        print(self.__name)

a = Test()
a.a()

print(Test.__name)
print(a.__name)
