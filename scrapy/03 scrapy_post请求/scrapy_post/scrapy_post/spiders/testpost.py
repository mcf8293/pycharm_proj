import json

import scrapy


class TestpostSpider(scrapy.Spider):
    name = "testpost"
    allowed_domains = ["https://fanyi.baidu.com/sug"]
    """
    post请求如果没有参数，那么这个请求将没有意义
    故：start_urls,parse方法无法使用
    需要重写start_request方法
    """
    def start_requests(self):
        url="https://fanyi.baidu.com/sug"
        data={
            'kw':'final'
        }
        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    def parse_second(self,response):
        content=response.text
        str_json=json.loads(content)
        print(str_json)
