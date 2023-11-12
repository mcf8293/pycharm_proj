import os
import re

from lxml import etree
import requests



if __name__ == '__main__':
    url='http://pic.netbian.com/4kmeinv'
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
    }
    response=requests.get(url=url, headers=headers)
    response.encoding="gbk"
    home_page=response.text
    # 创建图片文件夹
    if not os.path.exists('./pic'):
        os.makedirs('./pic')
    # 数据解析
    tree=etree.HTML(home_page)
    li_list=tree.xpath('//div[@class="slist"]/ul/li')
    for li in li_list:
        img_url='http://pic.netbian.com'+li.xpath('./a/@href')[0]
        img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
        img_html=requests.get(url=img_url,headers=headers).text
        img_ordinaroy=re.findall('data-pic="(.*?)"',img_html)[0]
        img_src='https://pic.netbian.com/'+img_ordinaroy
        # 存储图片
        img_path='pic/'+img_name
        with open(img_path,'wb') as f:
            f.write(requests.get(url=img_src).content)
        print(img_name,'下载成功')


