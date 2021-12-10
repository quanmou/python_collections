"""
动态定义变量
"""


"""使用python3内置函数exec，它支持python代码的动态执行"""
for i in range(5):
    exec('var{} = {}'.format(i, i))
    # exec(f'var{i} = {i}')

print(var0, var1, var2, var3, var4)


"""利用命名空间动态赋值"""
names = locals()
for i in range(5):
    names[f'n{i}'] = i

print(n0, n1, n2, n3, n4)


"""调用动态变量，利用exec函数"""
for i in range(5):
    exec('print(var{}, end=" ")'.format(i))


"""调用动态变量，利用命名空间"""
names = locals()
for i in range(5):
    print(names.get(f'var{i}'), end=' ')
