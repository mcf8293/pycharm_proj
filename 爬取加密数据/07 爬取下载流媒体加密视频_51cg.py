
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
    id=int(input("请输入番号："))
    url = f'https://hvedz2.btqdrp.com/archives/{id}/'
    # base_url = url.rsplit('/', 3)[0]  # https://hvedz2.btqdrp.com
    html_data = get_response(url).text
    title = re.findall(r'<title>(.*?)</title>', html_data)[0].split('!')[0]
    m3u8_url = re.findall('"video":{"url":"(.*?)"', html_data, re.S)[0]
    m3u8_url = m3u8_url.replace("\\", "")

    video_url = get_response(m3u8_url).text
    # 处理m3u8文件
    m3u8_data = re.sub('#E.*', '', video_url)
    # 将字符串转为列表
    ts_list = m3u8_data.split()

    # 密钥url
    key_url = re.findall('URI="(.*?)"', video_url, re.S)[0]
    base_key_url=key_url.rsplit('/', 2)[0]
    # 密钥ID
    key_id = key_url.split('/')[-2]

    # 密钥key
    key_ = key_url.split('=')[-1]

    # 密钥链接
    key_url = f'{base_key_url}/{key_id}/crypt.key?auth_key={key_}'

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
        ts_content = get_response(ts).content
        # 解密
        content = ci.decrypt(ts_content)
        with open(filename + title + '.mp4', mode="ab") as f:
            f.write(content)
    print("下载完成")
