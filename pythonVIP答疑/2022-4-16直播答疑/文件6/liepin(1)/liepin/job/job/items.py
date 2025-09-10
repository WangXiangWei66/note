# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    name = scrapy.Field()
    company = scrapy.Field()
    job_properties = scrapy.Field()
    job_desc = scrapy.Field()
