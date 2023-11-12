import time

import requests
from bs4 import BeautifulSoup


# 发送请求并解析页面
def get_html(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


if __name__ == '__main__':
    DOMAIN = "https://www.umei.cc"
    URL = "https://www.umei.cc/meinvtupian/meinvxiezhen/"
    homepage = get_html(URL)
    alist = homepage.find("div", attrs={"class": "listlbc_cont_l"}).find_all("a", attrs={"class": "img_album_btn"})
    for a in alist:
        # 拼接子页面的url
        detail_pages = URL + a.get("href").split("/")[-1]
        # 再次发送请求并解析
        child_page = get_html(detail_pages)
        # 获取子页面总页数
        num_tag = child_page.find("div", class_="pages").find_all("li")[-1].find("a")
        num_url = num_tag.get("href")
        # 获取子页面分页数
        num = int(num_url.split("/")[-1].split("_")[-1].split(".")[0])
        url_name = num_url.split("/")[-1].split("_")[0]
        # 处理第一页的网址链接
        for i in range(1, num + 1):
            if i<2:
                next_html = URL + url_name +  ".htm"
            else:
                next_html = URL + url_name + "_" + str(i) + ".htm"
            # 再次发送请求
            tag_htm=get_html(next_html)
            # 获取图片的真实地址
            src_url = tag_htm.find("div", class_="big-pic").find("img").get("src")
          # 再一次发送请求
            img_resp = requests.get(src_url)
            # 拼接文件名
            filename = src_url.split("/")[-1]
            # 保存图片
            f = open("pic/" + filename, mode="wb")
            f.write(img_resp.content)
            # 下载提示
            time.sleep(1)
            print(filename + "下载完成")
