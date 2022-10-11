"""
使用tasks封装两个协程，协程遇到耗时的操作时，会切换执行
"""
import threading
import asyncio


"""
以下程序会先打印两个"Hello world!"，等待1秒，再打印两个"Hello again!"
并且打印的4个线程id都是一样的，说明协程共用一个线程
"""
def main1():
    @asyncio.coroutine
    def hello():
        print("Hello world! (%s)" % threading.currentThread())
        yield from asyncio.sleep(1)
        print("Hello again! (%s)" % threading.currentThread())

    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]  # 封装两个coroutine
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


"""
以下程序会先打印1、3，过了2秒，打印2、4
"""
def main2():
    async def func1():
        print(1)
        await asyncio.sleep(2)  # 遇到耗时的操作，跳转到func2
        print(2)

    async def func2():
        print(3)
        await asyncio.sleep(2)  # 遇到耗时的操作，跳转到func1
        print(4)

    tasks = [
        asyncio.ensure_future(func1()),  # 3.7版本之后ensure_future改为create_task
        asyncio.ensure_future(func2())
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


main2()
