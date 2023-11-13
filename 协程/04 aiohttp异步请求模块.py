import asyncio
import os
import aiohttp

urls=[
    "https://www.umei.cc/d/file/20230521/8e2aa6031a21515beaa01cb168cf8c26.jpg",
    "https://www.umei.cc/d/file/20230520/4ff3cbd4f99704e000eb087f5494d9dd.jpg",
    "https://www.umei.cc/d/file/20230519/b9a112a4d22a34e82fe9a11058feddf6.jpg"
]

async def aiodownload(url):
    # 获取文件名
    name=url.rsplit("/", 1)[1]
    # 发送请求
    # 获取图片内容
    # 保存到文件
    filename = 'img\\'
    if not os.path.exists(filename):
        os.mkdir(filename)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open("img/"+name,mode="wb") as f:
                f.write(await resp.read()) # 读取内容是异步的. 需要await挂起, resp.text()
    print(name,"下载完成")


async def main():
    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    """
       raise RuntimeError('Event loop is closed')
RuntimeError: Event loop is closed
    """
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

