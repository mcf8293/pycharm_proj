import json
import os
import re
from tqdm import tqdm  # 进度条库
import requests
from Crypto.Cipher import AES


def get_response(url):
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
    }
    response = requests.get(url=url, headers=headers)
    return response


if __name__ == '__main__':
    url = 'https://74maoby.com/maoplay/190350_1_1.html'
    resp = get_response(url)
    resp.encoding = 'utf-8'
    html_data = resp.text
    title = re.findall(r"document.title='(.*?)'", html_data, re.S)[0]
    """m3u8文件有两重，第一次获取的m3u8文件里面包含另一个m3u8文件地址"""
    info = re.findall(r'<script type="text/javascript">var player_aaaa=(.*?)<', html_data)[0]
    # 将info转成字典（json数据）
    json_data = json.loads(info)
    # 字典取值，提取链接地址
    first_url = json_data['url']
    # 提取域名
    domain_url = first_url.rsplit('/', 3)[0]
    m3u8_first = get_response(first_url).text
    """
    第一重m3u8文件：
    #EXTM3U
    #EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1000000,RESOLUTION=1280x720
    /20200814/2VPTCEV9/1000kb/hls/index.m3u8
    """
    # 提取第二重m3u8连接地址
    m3u8_url = re.sub('#E.*', '', m3u8_first).strip()
    m3u8_url = domain_url + m3u8_url
    m3u8_orginal = get_response(m3u8_url).text
    # # 处理m3u8文件
    m3u8_data = re.sub('#E.*', '', m3u8_orginal)
    # 将字符串转为列表
    ts_list = m3u8_data.split()
    # 密钥
    key_ = re.findall('URI="(.*?)"', m3u8_orginal)[0]
    key_url = f"{domain_url}{key_}"
    # print("key_url: " + key_url) https://vip1.bfbfhao.com/20200814/2VPTCEV9/1000kb/hls/key.key
    # 发送请求获取密钥
    key = get_response(key_url).content
    # 解码器
    ci = AES.new(key, AES.MODE_CBC)
    # 存放视频目录
    filename = f'{title}\\'
    if not os.path.exists(filename):
        os.mkdir(filename)

    for ts in tqdm(ts_list):
        # 获取视频内容<加密数据>
        ts = domain_url + ts  # m3u8文件ts连接不完整，需要拼接
        ts_content = get_response(ts).content
        # 解密
        content = ci.decrypt(ts_content)
        with open(filename + title + '.mp4', mode="ab") as f:
            f.write(content)
