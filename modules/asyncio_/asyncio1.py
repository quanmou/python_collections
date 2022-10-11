"""
asyncio是python3.4版本引入的标准库，内置了对异步IO的支持
"""

import asyncio

"""
@asyncio.coroutine把一个generator标记为coroutine类型
"""
@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)    # asyncio.sleep()也是一个coroutine，yield from语法可以让我们方便地调用另一个generator
    print("Hello again!")  # 等待1秒，才会打印


"""
从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
Python3.8之后 @asyncio.coroutine 装饰器就会被移除
"""
async def hello2():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


loop = asyncio.get_event_loop()  # 获取EventLoop
loop.run_until_complete(hello())  # 执行coroutine
loop.close()


"""
yield form关键字是在Python3.3中引入的
yield from x 表达式对 x 对象所做的第一件事是，调用 iter(x)，从中获取迭代器。常用来替代内层for循环。
"""
def main1():
    def func1():
        yield 1
        yield from func2()
        yield 2

    def func2():
        yield 3
        yield 4

    f1 = func1()
    for item in f1:
        print(item)


"""
从python3.5引入的await用来替代yield from
"""
def main2():
    async def others():
        print("start")
        await asyncio.sleep(2)
        print('end')
        return '返回值'

    async def func():
        print("执行协程函数内部代码")
        # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
        response = await others()
        print("IO请求结束，结果为：", response)

    asyncio.run(func())


main2()
