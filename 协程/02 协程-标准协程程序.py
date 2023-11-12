import asyncio
import time

async def func1():
    print("我叫周杰伦")
    #time.sleep(3) # 当程序出现了同步操作时，异步就中断了
    await asyncio.sleep(3) # 异步操作的代码
    print("我是joy")

async def func2():
    print("我叫林俊杰")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("我是jj")

async def func3():
    print("我叫蔡依林")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("我是jolin")

if __name__ == '__main__':
    f1=func1()
    f2=func2()
    f3=func3()
    tasks=[f1,f2,f3]
    # 一次启动多个任务（协程）
    t1=time.time()
    asyncio.run(asyncio.wait(tasks))
    t2=time.time()
    print(t2-t1)

