import os
import re
import aiohttp
import asyncio

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}


async def get_response(session, url):
    async with session.get(url, headers=headers) as response:
        return await response.text()


# 获取主页图片链接
def get_img_urls(html):
    img_originals = re.findall('<div class="img">.*?<a href="(.*?)">', html, re.S)
    img_urls = ['https://www.umei.cc' + item for item in img_originals if not item.startswith('http')]
    return img_urls


# 获取详情页图片链接
def get_img_src(html):
    img_src = re.findall('<div class="big-pic">.*?<img alt=.*?src="(.*?)" />', html, re.S)
    img_title=re.findall('<h1>(.*?)</h1>',html,re.S)
    return img_src


# 保存图片
async def save_img(session, img_src):
    filename = img_src.split('/')[-1]
    filepath = os.path.join('imgs', filename)
    if not os.path.exists('imgs'):
        os.mkdir('imgs')
    async with session.get(img_src, headers=headers) as response:
        with open(filepath, 'wb') as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)

    print(f'{filename} 下载成功')

async def main():
    url = "https://www.umei.cc/bizhitupian/meinvbizhi/index_3.htm"
    async with aiohttp.ClientSession() as session:
        html = await get_response(session, url)
        img_urls = get_img_urls(html)
        tasks = []
        for img_url in img_urls:
            img_html = await get_response(session, img_url)
            img_srcs = get_img_src(img_html)
            for img_src in img_srcs:
                tasks.append(save_img(session, img_src))
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
