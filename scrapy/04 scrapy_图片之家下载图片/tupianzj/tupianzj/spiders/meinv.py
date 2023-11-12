import re

import scrapy

# 将cookie字符串转换为字典
def cookie_convert_dict(cookie_string):
    # 创建一个空字典
    mydic={}
    # 将cookie字符串按照分号空格拆分成列表
    for item in cookie_string.split('; '):
        # 将每一项拆分成key和value
        key, value = item.split('=')
        # 将key和value添加到字典中
        mydic[key.strip()]=value.strip()
    # 返回字典
    return mydic

class MeinvSpider(scrapy.Spider):
    name = "meinv"

    #自定义headers
    def start_requests(self):
        url="https://www.tupianzj.com/bizhi/DNmeinv/"
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
                  }

        cookie_str="""        
        t=c45d2f297e2c388e92278cfaacc3c7cf; r=346; Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1699067809,1699073758; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1699073758
        """
        mydic=cookie_convert_dict(cookie_str)

        yield scrapy.Request(url=url,method="get",headers=headers,cookies=mydic,callback=self.parse)


   # 定义parse函数，用于解析列表页，并获取详情页的链接
    def parse(self, resp,**kwargs):
        # 获取列表页中所有li标签
        li_list=resp.xpath("//ul[@class='list_con_box_ul']/li")
        # 遍历li标签
        for li in li_list:
            # 获取li标签中的a标签的href属性
            href=li.xpath("./a/@href").extract_first()
            # 构造详情页的链接
            yield scrapy.Request(
                url=resp.urljoin(href),
                # 请求方式为get
                method="get",
                # 回调函数为parse_detail
                callback=self.parse_detail
            )


    def parse_detail(self,resp,**kwargs):
      pass



