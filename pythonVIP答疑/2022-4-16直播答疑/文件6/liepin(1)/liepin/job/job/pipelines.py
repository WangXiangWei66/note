# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

from  pymongo import MongoClient

class JobPipeline:
    def open_spider(self,spider):
        self.client = MongoClient()#创建数据库
        self.liepin = self.client.liepin.job #创建库

    def process_item(self, item, spider):
        #self.liepin.insert(dict(item))
        self.liepin.insert_one(dict(item))

    def close_spider(self,spider):
        self.client.close()
