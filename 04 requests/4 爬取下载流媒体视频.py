import json
import os
import re
import requests
from tqdm import tqdm



def get_response(url):
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
    }
    response = requests.get(url=url, headers=headers)
    return response


if __name__ == '__main__':
    url = 'https://www.acfun.cn/v/ac13941759'
    html_data = get_response(url).text
    title = re.findall('"title":"(.*?)",', html_data)[1]
    info = re.findall(r'window.pageInfo = window.videoInfo = (.*?);', html_data)[0]
    # 将info转成字典（json数据）
    json_data = json.loads(info)
    # 字典取值，提取链接地址
    m3u8_url = \
        json.loads(json_data['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['backupUrl'][0]
    # 获取m3u8数据
    m3u8_orginal = get_response(m3u8_url).text
    # 处理m3u8文件
    m3u8_data = re.sub('#E.*', '', m3u8_orginal)

    # 将字符串转为列表
    ts_list = m3u8_data.split()
    # 存放视频目录
    filename = f'{title}\\'
    if not os.path.exists(filename):
        os.mkdir(filename)
    # 下载ts视频片段
    num = 1
    for ts in tqdm(ts_list):

        ts_url = 'https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/'+ts
        ts_content = get_response(ts_url).content
        with open(filename + title +str(num)+ '.ts', mode="wb") as f:
            f.write(ts_content)
        num += 1

    # 下载视频文件
    # for ts in tqdm(ts_list):
    #     ts_url = 'https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/' + ts
    #     ts_content = get_response(ts_url).content
    #     with open(filename + title +  '.mp4', mode="ab") as f:
    #         f.write(ts_content)

