
import os
import re
import aiohttp
import asyncio


class WebScraper:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        self.session = None

    async def get_response(self, url):
        async with self.session.get(url, headers=self.headers) as response:
            return await response.text()

    def get_img_urls(self, html):
        img_originals = re.findall('/tupian/\d+\.html', html, re.S)
        img_urls = ['https://pic.netbian.com' + item for item in img_originals if not item.startswith('http')]
        return img_urls

    def get_img_src(self, html):
        img_src = re.findall('<img src.*?data-pic="(.*?)"', html, re.S)
        return img_src

    async def save_img(self, img_src):
        filename = img_src.split('/')[-1]
        filepath = os.path.join('imgs_4k', filename)
        if not os.path.exists('imgs_4k'):
            os.mkdir('imgs_4k')
        async with self.session.get(img_src, headers=self.headers) as response:
            with open(filepath, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)

        print(f'{filename} 下载成功')

    async def scrape_page(self, page_num):
        url = self.base_url + str(page_num) + ".htm"
        html = await self.get_response(url)
        img_urls = self.get_img_urls(html)
        tasks = []
        for img_url in img_urls:
            img_html = await self.get_response(img_url)
            img_srcs = self.get_img_src(img_html)
            for img_src in img_srcs:
                tasks.append(self.save_img(img_src))
        await asyncio.gather(*tasks)

    async def scrape_website(self, start_page=2, end_page=5):
        async with aiohttp.ClientSession() as session:
            self.session = session
            for page_num in range(start_page, end_page):
                await self.scrape_page(page_num)

if __name__ == '__main__':
    scraper = WebScraper("https://pic.netbian.com/4kyingshi/index_")
    asyncio.run(scraper.scrape_website())