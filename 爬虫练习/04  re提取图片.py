import os
import requests,re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# 获取主页源代码
def get_response(url):
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    return response.text

# 获取主页图片链接
def get_img_url(url):
    img_originals = re.findall('<div class="img">.*?<a href="(.*?)">',url,re.S)
    img_urls=['https://www.umei.cc'+item for item in img_originals]
    return img_urls

# 获取详情页图片链接
def get_img_src(html):
    img_src = re.findall('<div class="big-pic">.*?<img alt=.*?src="(.*?)" />',html,re.S)
    return img_src

# 保存图片
def save_img(img_src):
    filepath = os.path.join("imgs","")
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    img_name = img_src.split('/')[-1]
    img = requests.get(img_src,headers=headers)
    with open(os.path.join(filepath,img_name),'wb') as f:
        f.write(img.content)
        print(img_name,'下载成功')


if __name__ == '__main__':
    url = "https://www.umei.cc/bizhitupian/meinvbizhi/index_3.htm"
    html = get_response(url)
    img_urls=get_img_url(html)
    for img_url in img_urls:
        img_srcs=get_img_src(get_response(img_url))
        for img_src in img_srcs:
            save_img(img_src)







