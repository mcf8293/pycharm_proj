import re
import time
from pprint import pprint

import aiohttp
import asyncio



class AsyncSpider:
    # 异步请求url
    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text(encoding='utf-8')

    # 解析数据
    async def parse(self, html):
        titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>',html, re.DOTALL)
        poems=re.findall(r'<div class="contson".*?>(.*?)</div>',html, re.DOTALL)
        # 使用列表推导式去掉诗歌内容中\n和<br>标签
        contents = [item.replace('\n', '').replace('<br />', '') for item in poems]
        return {"title": titles, "contents": contents}

    # 异步请求url
    async def fetch_and_parse(self, url):
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, url)
            return await self.parse(html)

    # 保存数据
    def save_data(self, titles, poems):
        return titles,poems

    async def crawl(self, urls):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(self.fetch_and_parse(url))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
        return results


    def run(self, urls):
        start = time.time()
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(self.crawl(urls))
        end = time.time()
        print('总耗时:', end - start)
        return results

if __name__ == '__main__':
    urls = [f'https://www.gushiwen.org/default_%d.aspx' % i for i in range(1, 2, 1)]
    spider = AsyncSpider()
    results = spider.run(urls)
    for result in results:
        title=result['title']
        poem=result['contents']
        print("title:",title)
        print("poem:",poem)