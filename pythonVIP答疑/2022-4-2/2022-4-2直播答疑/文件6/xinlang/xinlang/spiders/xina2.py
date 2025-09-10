import scrapy
from xinlang.items import XinlangItem


class Xina2Spider(scrapy.Spider):
    name = 'xina2'
    # allowed_domains = ['xina.com']
    start_urls = ['https://news.sina.com.cn/china/']


    def parse(self, response): # response是一个响应对象
        item = XinlangItem()


        title = response.xpath('//div[@class="feed-card-item"]/h2/a') # 使用xpath提取数据
        print(response) # 有响应，响应的状态码是200
        title_list = []
        for i in range(len(title)):
            title_list.append(title[i].get_text())
        item['title'] = title_list
        print(title)  # 没有提取到数据
        yield item
