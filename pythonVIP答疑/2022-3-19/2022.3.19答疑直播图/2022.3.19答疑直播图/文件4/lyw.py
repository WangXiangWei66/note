import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LieyunItem


class LywSpider(CrawlSpider):
    name = 'lyw'
    allowed_domains = ['lieyunwang.com']
    start_urls = ['https://www.lieyunwang.com/latest/p1.html']#这是从第一页开始

    rules = (#把规则写好，自己就可以提取网址
        Rule(LinkExtractor(allow=r'/latest/p\d+.html'), follow=True),#规则是什么。是否继续跟进，不需要解析
        Rule(LinkExtractor(allow=r'/archives/\d+'), callback='parse_item', follow=False),#不需要跟进，需要解析

    )

    def parse_item(self, response):
        title_lst = response.xpath('//h1[@class="lyw-article-title-inner"]/text()').getall()
        title=''.join(title_lst).strip()
        time= response.xpath('//h1[@class="lyw-article-title-inner"]/span/text()').get()
        author_name=response.xpath('//a[@class="author-name open_reporter_box"]/text()').get()
        #   其实//a[contains(@class,'author_name')]也是可以对，这是xpath的一种包含的语法
        txt_lst=response.xpath('//div[@class="main-text"]/p/text()').getall()
        main_text=''.join(txt_lst).strip()
        print(title,"\n",time,"\n",author_name,"\n",main_text)
        print(response.url)
        article_url=response.url

        #创建item对象
        item=LieyunItem()
        item['title']=title
        item['time'] = time
        item['author_name'] = author_name
        item['time'] = time
        item['main_text'] =main_text

        yield item



        #print(title)



        #print(response.url)
        #item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        #return item
