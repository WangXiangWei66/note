# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    titlte=scrapy.Field()
    author=scrapy.Field()
    people=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
