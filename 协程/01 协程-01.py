import asyncio
import time

async def func():
    print("hello world")

if __name__ == '__main__':
    g=func() # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
    asyncio.run(g) # 协程程序运行需要asyncio模块支持