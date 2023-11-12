import scrapy
from dytt.items import DyttItem

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.ygdy8.net"]
    start_urls = ["https://www.ygdy8.net/html/gndy/china/index.html"]

    def parse(self, response,**kwargs):
        links=response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for link in links:
            name=link.xpath('./text()').extract_first()
            url=link.xpath('./@href').extract_first()
            # 拼接详情页的url
            url='https://www.ygdy8.net'+url
            # 带参数对详情页发送请求
            yield scrapy.Request(url=url,callback=self.parse_details,meta={"name":name})

    def parse_details(self, response,**kwargs):
        src=response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # 接收到请求的那个meta参数的值
        name=response.meta["name"]
        movie=DyttItem(name=name,src=src)
        yield movie