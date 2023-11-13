import json
import os
import re
import aiohttp
import asyncio
from tqdm import tqdm


async def get_response(session, url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
    }
    async with session.get(url, headers=headers) as response:
        return await response.text()


async def download_ts_file(session, ts_url, filename):
    async with session.get(ts_url) as response:
        content = await response.read()
        with open(filename, mode="wb") as f:
            f.write(content)


async def main():
    url = 'https://www.acfun.cn/v/ac13941759'
    async with aiohttp.ClientSession() as session:
        html_data = await get_response(session, url)
        title = re.findall('"title":"(.*?)",', html_data)[1]
        info = re.findall(r'window.pageInfo = window.videoInfo = (.*?);', html_data)[0]
        json_data = json.loads(info)
        m3u8_url = \
        json.loads(json_data['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['backupUrl'][0]
        m3u8_orginal = await get_response(session, m3u8_url)
        m3u8_data = re.sub('#E.*', '', m3u8_orginal)
        ts_list = m3u8_data.split()
        filename = f'{title}\\'
        if not os.path.exists(filename):
            os.mkdir(filename)
        tasks = []
        num = 1
        for ts in tqdm(ts_list):
            ts_filename = os.path.join(filename, f"{title}_{num}.ts")
            ts_url = 'https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/' + ts
            task = asyncio.create_task(download_ts_file(session, ts_url, ts_filename))
            tasks.append(task)
            num += 1
        # await asyncio.gather(*tasks)
        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())