import time

import requests
from bs4 import BeautifulSoup

url="https://96maonn.com/arttypehtml/38.html"
domain="https://96maonn.com"
resp=requests.get(url)
resp.encoding="utf-8"

home_page=BeautifulSoup(resp.text,"html.parser")
href_list=home_page.find("div",class_="text-list-html").find_all("a")
for a in href_list:
    # 拼接完整子页面链接地址
    href=domain+a.get("href")
    # 再次使用requests获取子页面的源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面获取图片的下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    # 获取图片的img标签
    img_tab = child_page.find("div", class_="content").find("img")
    # 利用get属性获取值
    src = img_tab.get("data-original")

    # 下载图片
    img_resp = requests.get(src)  # img_resp.conteent 这里获取的是字节
    # 获取文件名
    img_name = src.split("/")[-1]
    with open("img/" + img_name, mode="wb") as f:
        f.write(img_resp.content)  # 将图片内容写入文件
    print(f"{img_name}下载完成")
    time.sleep(1)
print("下载完毕")



