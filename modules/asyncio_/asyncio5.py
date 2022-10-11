"""
使用create_task来并发运行多个任务
使用asyncio.run()来执行任务
"""

import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return what[0]


"""
以下代码段会在等待 1 秒后打印 "hello"，然后 再次 等待 2 秒后打印 "world"
"""
async def main1():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


"""
使用create_task来并发运行多个任务，总体耗时为2秒
"""
async def main2():
    task1 = asyncio.create_task(say_after(1, 'hello'))  # 3.7版本之前，create_task可以改为ensure_future
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


"""
使用asyncio.wait(tasks)来等待多个任务结束，与main2一样，总体耗时为2秒
"""
async def main3():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    tasks = [task1, task2]

    print(f"started at {time.strftime('%X')}")
    await asyncio.wait(tasks)
    print(f"finished at {time.strftime('%X')}")


"""
可以通过await获取相应协程的返回值
"""
async def main4():
    task1 = asyncio.create_task(say_after(1, 'hello'))  # 3.7版本之前，create_task可以改为ensure_future
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    ret1 = await task1
    print(ret1)
    ret2 = await task2
    print(ret2)
    print(f"finished at {time.strftime('%X')}")


# 方式一
# loop = asyncio.get_event_loop() # 创建一个事件循环
# loop.run_until_complete(result) # 将协程当做任务提交到事件循环的任务列表中，协程执行完成之后终止。

# 方式二
# 本质上方式一是一样的，内部先 创建事件循环 然后执行 run_until_complete，一个简便的写法。
# asyncio.run 函数在 Python 3.7 中加入 asyncio 模块，
asyncio.run(main4())
