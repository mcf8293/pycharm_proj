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
    url = 'https://fedfby11.com/video/show/id/135126'
    html_data = get_response(url).text
    title = re.findall(r'<title>(.*?)</title>', html_data)[0]
    m3u8_url = re.findall(r"var url = '(.*?)'", html_data, re.S)[0]
    base_url = m3u8_url.rsplit('/', 1)[0]
    m3u8_orginal = get_response(m3u8_url).text
    # 处理m3u8文件
    m3u8_data = re.sub('#E.*', '', m3u8_orginal)
    # 将字符串转为列表
    ts_list = m3u8_data.split()
    # 密钥
    key_ = re.findall('URI="(.*?)"', m3u8_orginal)[0]
    key_url = f"{base_url}/{key_}"
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
        ts = base_url + "/" + ts #m3u8文件ts连接不完整，需要拼接
        ts_content = get_response(ts).content
        # 解密
        content = ci.decrypt(ts_content)
        with open(filename + title + '.mp4', mode="ab") as f:
            f.write(content)
