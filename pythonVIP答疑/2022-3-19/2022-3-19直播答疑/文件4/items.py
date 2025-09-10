# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LieyunItem(scrapy.Item):
    title=scrapy.Field()
    time=scrapy.Field()
    author_name=scrapy.Field()
    main_text=scrapy.Field()
    article_url=scrapy.Field()

