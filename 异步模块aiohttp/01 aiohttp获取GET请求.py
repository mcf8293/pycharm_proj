import asyncio
import re

import aiohttp

# 定义一个函数，参数为url，返回一个列表
urls = ['https://www.gushiwen.org/default_%s.aspx' % i for i in range(1, 3)]

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
}


# 异步下载函数
async def aiodownload(url):
    # 使用aiohttp库创建一个客户端会话
    async with aiohttp.ClientSession() as session:
        # 使用session.get函数发送get请求
        async with session.get(url, headers=headers) as resp:
            # 获取响应的文本
            text = await resp.text()
            # 使用正则表达式查找title标签中的文本
            title = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
            # 打印title标签中的文本
            print(title)


# 异步函数main，用于异步下载urls中的每一个url
async def main():
    # 创建一个空的任务列表
    tasks = []
    # 遍历urls中的每一个url
    for url in urls:
        # 将每一个url添加到任务列表中
        tasks.append(asyncio.create_task(aiodownload(url)))
    # 等待所有任务完成
    await asyncio.wait(tasks)


if __name__ == '__main__':
    """
       raise RuntimeError('Event loop is closed')
RuntimeError: Event loop is closed
    """
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # 异步执行main函数
    asyncio.run(main())
