import time
import aiohttp
import asyncio
from bs4 import BeautifulSoup


class AsyncSpider:
    async def fetch(self, session, url, data=None):
        async with session.post(url, data=data) as response:
            return await response.text(encoding='utf-8')

    async def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        # 提取标题和内容，根据网页结构进行修改
        title = soup.find('title').text.strip() if soup.find('title') else None
        content = soup.find('div', {'class': 'content'}).text.strip() if soup.find('div',
                                                                                   {'class': 'content'}) else None
        return {"title": title, "content": content}

    async def crawl(self, urls, data):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(self.fetch_and_parse(session, url, data))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
        return results

    async def fetch_and_parse(self, session, url, data):
        html = await self.fetch(session, url, data)
        data = await self.parse(html)
        return data

    def run(self, urls, data):
        start = time.time()
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(self.crawl(urls, data))
        end = time.time()
        print('总耗时:', end - start)
        return results

if __name__ == '__main__':

    spider = AsyncSpider()
    urls = ['http://example.com/page1', 'http://example.com/page2', 'http://example.com/page3']
    data = {'key1': 'value1', 'key2': 'value2'}  # 根据网站要求修改POST请求的参数
    results = spider.run(urls, data)

    for result in results:
        title = result.get("title")
        content = result.get("content")
        print("Title:", title)
        print("Content:", content)
        print("--------------------")