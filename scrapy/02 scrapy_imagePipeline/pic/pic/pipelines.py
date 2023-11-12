# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline


class PicPipeline:
    def process_item(self, item, spider):
        return item


class beautyPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return scrapy.Request(item['img_src'])

    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = request.url.split("/")[-1]
        return f"img/{file_name}"

    def item_completed(self, results, item, info):
        print(results)
