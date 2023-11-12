import re
import aiohttp
import asyncio

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

# 异步获取请求
async def get_request(url):
    # 使用aiohttp库创建一个ClientSession对象
    async with aiohttp.ClientSession() as session:
        # 使用session对象发送get请求
        async with session.get(url) as response:
            # 返回响应文本
            return await response.text()


# 单页获取
async def main():
    url="https://www.gushiwen.org/default_1.aspx"
    html=await get_request(url)
    title = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', html, re.DOTALL)
    print(title)



if __name__ == '__main__':

    asyncio.run(main())
