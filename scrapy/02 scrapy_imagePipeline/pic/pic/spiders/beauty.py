import scrapy


from pic.items import PicItem

class BeautySpider(scrapy.Spider):
    name = "beauty"
    allowed_domains = ["umei.cc"]
    start_urls = ["https://www.umei.cc/bizhitupian/meinvbizhi/"]

    def parse(self, resp,**kwargs):
        hrefs=resp.xpath("//div[@class='listlbc_cont_l']/div/div/div/div/div/a/@href").extract()
        for href in hrefs:
            yield scrapy.Request(
                url=resp.urljoin(href),
                method='GET',
                callback=self.parse_detail
            )

        # 爬取下一页数据
        next_href = resp.xpath("//div[@id='pageNum']/a[contains(text(),'下一页')]/@href").extract_first()
        if next_href:
            # print("Full page")
            yield scrapy.Request(
                url=resp.urljoin(next_href),
                method='GET',
                callback=self.parse
            )
        # else:
            # print("empty page")


    def parse_detail(self, resp,**kwargs):
        name=resp.xpath("//*[@id='photos']/h1/text()").extract_first()
        img_src=resp.xpath("//div[@class='big-pic']/a/img/@src").extract_first()
        item=PicItem()
        item["name"]=name
        item["img_src"]=img_src
        return item






