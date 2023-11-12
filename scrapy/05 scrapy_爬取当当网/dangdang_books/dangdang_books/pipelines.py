# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface



class DangdangBooksPipeline:
    def open_spider(self, spider):
        self.f = open("./book.csv", mode='a', encoding='utf-8')

    def close_spider(self, spider):
        if self.f:
            self.f.close()

    def process_item(self, item, spider):
        self.f.write (str(item)+"\n")
        return item
