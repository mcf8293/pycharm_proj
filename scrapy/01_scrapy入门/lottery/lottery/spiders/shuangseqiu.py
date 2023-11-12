import scrapy
from lottery.items import LotteryItem

class ShuangseqiuSpider(scrapy.Spider):
    name = "shuangseqiu"
    allowed_domains = ["500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    def parse(self, response,**kwargs):
        trs=response.xpath("//tbody[@id='tdata']/tr")
        for tr in trs:
            if tr.xpath("./@class").extract_first()=="tdbck":
                continue
            # red_ball=tr.xpath("./td[@class='chartBall01']/text().extract_first()")
            # blue_ball=tr.xpath("./td[@class='chartBall02']/text().extract_first()")
            number = tr.xpath("./td[1]/text()").extract_first().strip()
            red_ball=tr.css(".chartBall01::text").extract()
            blue_ball = tr.css(".chartBall02::text").extract_first()
            # 创建item对象，然后进行数据封装
            lottery=LotteryItem()
            lottery["number"]=number
            lottery["red_ball"]=red_ball
            lottery["blue_ball"]=blue_ball
            # 将item传送给pipelines
            yield lottery



