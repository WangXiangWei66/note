import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import JobItem


class LiepinSpider(CrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?key=python']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.liepin.com/job/\d+\.shtml.*'), callback='parse_item', follow=False),

    )

    def parse_item(self, response):
        # print(response.xpath('//div[@class="job-detail-box"]/a[@data-nick]/@href'))
        name = response.css('.name-box span::text').get() #职位名称
        company = response.css('.content .name.ellipsis-1::text').get() #公司名称
        job_properties = response.css('.job-properties span::text').getall() #任职要求，工作地点
        job_desc_lst = response.css('dd::text').getall() #职位秒是的列表
        job_desc = ''.join(job_desc_lst).strip() #职位描述

        #存储操作
        item = JobItem(name=name,
                       company=company,
                       job_properties=job_properties,
                       job_desc=job_desc)
        yield item
