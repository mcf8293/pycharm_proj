from urllib import request

import requests
from bs4 import BeautifulSoup


# 发送请求并解析页面
def get_html(url):
    response= requests.get(url)
    response.encoding="utf-8"
    soup= BeautifulSoup(response.text,"html.parser")
    return soup

if __name__ == '__main__':
    URL="https://www.umei.cc/meinvtupian/meinvxiezhen/"
    homepage=get_html(URL)
    alist=homepage.find("div",attrs={"class":"listlbc_cont_l"}).find_all("a",attrs={"class":"img_album_btn"})
    for a in alist:
        # 拼接子页面的url
        detail_pages=URL+a.get("href").split("/")[-1]
        # 再次发送请求并解析
        child_page=get_html(detail_pages)
        # 找到图片的真实地址
        src_url=child_page.find("div",class_="big-pic").find("img").get("src")
        # 再一次发送请求
        img_resp=requests.get(src_url)
        # 拼接文件名
        filename=src_url.split("/")[-1]
        # 保存图片
        f=open("pic/"+filename,mode="wb")
        f.write(img_resp.content)
        # 下载提示
        print(f"{filename}下载完成")


