import os
import re
import aiohttp
import asyncio

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# 获取主页源代码
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
    return img_src

# 异步函数，用于保存图片
async def save_img(session, img_src):
    # 获取图片文件名
    filename = img_src.split('/')[-1]
    # 设置图片文件路径
    filepath = os.path.join('imgs', filename)
    # 如果imgs文件夹不存在，则创建
    if not os.path.exists('imgs'):
        os.mkdir('imgs')
    # 使用session发起get请求，获取图片内容
    async with session.get(img_src, headers=headers) as response:
        # 使用with open语句，以二进制写入模式，打开文件
        with open(filepath, 'wb') as f:
            # 循环读取图片内容，写入文件
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)

    print(f'{filename} 下载成功')


async def main():
    base_url = "https://www.umei.cc/bizhitupian/meinvbizhi/index_"
    for page_num in range(3,6):
        url=base_url+str(page_num)+".htm"
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
