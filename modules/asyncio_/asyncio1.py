"""
python3.4版本引入的标准库，内置了对异步IO的支持
"""

import asyncio


@asyncio.coroutine  # @asyncio.coroutine把一个generator标记为coroutine类型
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)    # asyncio.sleep()也是一个coroutine，yield from语法可以让我们方便地调用另一个generator
    print("Hello again!")  # 不会等待1秒，会直接执行


loop = asyncio.get_event_loop()  # 获取EventLoop
loop.run_until_complete(hello())  # 执行coroutine
loop.close()
