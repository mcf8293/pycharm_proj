# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
import pymysql.cursors
import lottery.settings as settings
import csv
class LotteryPipeline:
    def open_spider(self, spider):
        self.f = open("./双色球.csv", mode='a', encoding='utf-8')

    def close_spider(self, spider):
        if self.f:
            self.f.close()

    def process_item(self, item, spider):
        self.f.write(f"{item['number']},{'_'.join(item['red_ball'])},{item['blue_ball']}\n")
        return item

class LotteryCSVPipeline:
    def open_spider(self, spider):
        self.f = open("./csv_ball.csv", mode='a', encoding='utf-8')
        self.writer=csv.writer(self.f)
        # 写入csv文件的表头
        self.writer.writerow(["期号","红球","蓝球"])


    def process_item(self, item, spider):
        # 讲爬取的数据写入csv文件
        self.writer.writerow([item['number'],item['red_ball'],item['blue_ball']])
        return item

    def close_spider(self, spider):
        if self.f:
            self.f.close()
# 保存数据到mysql数据库
class LotteryMySQLPipeline:
    def __init__(self):
        self.conn = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWORD,
            database=settings.MYSQL_DBNAME
        )

    def close_spider(self, spider):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        global cursor
        try:
            cursor = self.conn.cursor()
            sql = "insert into caipiao(number,red_ball,blue_ball) values (%s,%s,%s)"
            cursor.execute(sql, (item['number'], '_'.join(item['red_ball']), item['blue_ball']))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            cursor.close()

        return item
