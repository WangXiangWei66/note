# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter


class SunproPipeline:
    def __init__(self):
        self.f = open('电影.csv', mode="a", encoding="utf-8", newline='')

    def process_item(self, item, spider):
        d = dict(item)
        self.f.writelines(str(d))

        return item


    def close_spier(self,spider):
        self.f.close()