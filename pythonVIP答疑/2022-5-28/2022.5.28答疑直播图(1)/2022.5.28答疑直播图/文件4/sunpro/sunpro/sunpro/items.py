# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#items
import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    new_sum = scrapy.Field()
    new_title = scrapy.Field()

class DetailItem(scrapy.Item):
    new_id = scrapy.Field()
    new_content = scrapy.Field()
