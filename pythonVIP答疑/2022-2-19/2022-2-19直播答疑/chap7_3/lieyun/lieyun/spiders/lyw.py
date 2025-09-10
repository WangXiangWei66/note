# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import  LieyunItem

class LywSpider(CrawlSpider):
    name = 'lyw'
    allowed_domains = ['lieyunwang.com']
    start_urls = ['https://www.lieyunwang.com/latest/p1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/latest/p\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'/archives/\d+'),callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title_lst = response.xpath('//h1[@class="lyw-article-title-inner"]/text()').getall()
        title=''.join(title_lst).strip()   # 标题
        publish_time=response.xpath('//h1[@class="lyw-article-title-inner"]/span/text()').get() #发布时间

        author_name=response.xpath('//a.txt[contains(@class,"author-name")]/text()').get() # 作者
        content= response.xpath('//div[@class="main-text"]//text()').getall()
        content=''.join(content).strip()
        article_url=response.url

        #创建Item的对象
        item=LieyunItem()
        item['title']=title
        item['author']=author_name
        item['publish_time']=publish_time
        item['content']=content
        item['article_url']=article_url

        yield item

