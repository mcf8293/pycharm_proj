import asyncio
import time

async def func1():
    print("我叫周杰伦")
    await asyncio.sleep(3)
    print("我是joy")

async def func2():
    print("我叫林俊杰")
    await asyncio.sleep(2)
    print("我是jj")

async def func3():
    print("我叫蔡依林")
    await asyncio.sleep(4)
    print("我是jolin")

async def main():

    # 标准写法
    """
    tasks=[func1(), func2(), func3()]
    DeprecationWarning: The explicit passing of coroutine objects to asyncio.wait() is deprecated since Python 3.8, and scheduled for removal in Python 3.11.
  await asyncio.wait(tasks)
   应修改为：
   tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]

    """
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    start=time.time()
    asyncio.run(main())
    end=time.time()
    print(end-start)


