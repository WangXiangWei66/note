# -*- coding: utf-8 -*-
import scrapy


class LieyunwangSpider(scrapy.Spider):
    name = 'lieyunwang'
    allowed_domains = ['lieyunwang.com']
    start_urls = ['http://lieyunwang.com/']

    def parse(self, response):
        pass
