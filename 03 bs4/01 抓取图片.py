"""
下载中间件的使用.txt：
 1.获取主页面的源代码，然后提取子页面的链接地址
 2.通过子页面的内容，提取图片的下载链接
 3，下载图片
"""
import requests
from bs4 import BeautifulSoup
import time
url="https://www.umei.cc/bizhitupian/meinvbizhi/"
domain="https://www.umei.cc"
resp=requests.get(url)
resp.encoding="utf-8" # 处理乱码
#把源代码交给bs
home_page=BeautifulSoup(resp.text,"html.parser")
href_list=home_page.find("div",class_="item_list infinite_scroll").find_all("a")
# 利用set()函数去掉重复链接
hlist=set(href_list)
for a in hlist:
    href=domain+a.get("href") # 通过get获取属性值
    # 获取子页面的源代码
    child_page_resp=requests.get(href)
    child_page_resp.encoding="utf-8"
    child_page_text=child_page_resp.text
    # 从子页面获取图片的下载路径
    child_page=BeautifulSoup(child_page_text,"html.parser")
    img_tab=child_page.find("div",class_="big-pic").find("img")
    src=img_tab.get("src")
    # 下载图片
    img_resp=requests.get(src)
    # img_resp.conteent 这里获取的是字节
    # 获取文件名
    img_name=src.split("/")[-1]
    with open("img/"+img_name,mode="wb")as f:
        f.write(img_resp.content) # 将图片内容写入文件
    print(f"{img_name}下载完成")
    time.sleep(1)
print("下载完毕")












