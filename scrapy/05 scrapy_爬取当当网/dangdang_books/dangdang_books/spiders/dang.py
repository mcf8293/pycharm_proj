import scrapy
from dangdang_books.items import DangdangBooksItem


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]

    def parse(self, response, **kwargs):
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # 由于网页图片使用懒加载技术，所有需要对图片地址进行判断
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = "https:" + src
            else:
                src = "https:" + li.xpath('.//img/@src').extract_first()
            alt = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[2]/text()').extract_first()
            item = DangdangBooksItem(name=alt,src=src,price=price)
            yield item
