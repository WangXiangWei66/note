#主文件
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SunproItem,DetailItem

class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']
    #链接提取器：根据指定规则（allow="正则"）进行指定链接的提取
    link = LinkExtractor(allow=r'id=1&page=\d+')
    link_detail = LinkExtractor(allow=r'id=\d+')
    rules = (
        #规则解析器:将链接提取器提取到的链接进行指定规则（callback）的解析操作
        Rule(link, callback='parse_item', follow=True),
        #follow=True：可以将链接提取器 继续做用到 链接提取器提取到的链接 所对应的页面中
        Rule(link_detail,callback='parse_detail',follow=True)
    )
    #解析编号和新闻标题
    #如下俩个解析方法中是不能实现请求传参的
    #如果将俩个解析方法解析的数据存储到同一个item中，可以依次存储到俩个item
    def parse_item(self, response):
        li_list = response.css('ul.title-state-ul li')
        for li in li_list:
            new_num = li.css('span.state1::text').extract
            new_title = li.css('span.state3 a::text').extract
            #print(new_num,new_title)  用于测试程序是否出错
            item = SunproItem()
            item['new_num'] = new_num
            item['new_title']=new_title
            yield item
    #解析新闻编号和新闻内容
    def parse_detail(self,response):
        new_id = response.css('span.fl.details-head img::text').extract()
        new_content = response.css('div.details-box pre::text').extract()
        item = DetailItem()
        item['new_id']=new_id
        item['new_content']=new_content
        yield item
