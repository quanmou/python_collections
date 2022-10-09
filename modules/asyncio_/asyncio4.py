"""
从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
"""
import asyncio

"""
旧写法
"""
@asyncio.coroutine
def hello1():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")


"""
新写法
"""
async def hello2():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


loop = asyncio.get_event_loop()
loop.run_until_complete(hello2())
loop.close()
