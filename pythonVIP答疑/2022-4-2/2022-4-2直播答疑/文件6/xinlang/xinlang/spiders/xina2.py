import scrapy
from xinlang.items import XinlangItem


class Xina2Spider(scrapy.Spider):
    name = 'xina2'
    # allowed_domains = ['xina.com']
    start_urls = ['https://news.sina.com.cn/china/']


    def parse(self, response): # response��һ����Ӧ����
        item = XinlangItem()


        title = response.xpath('//div[@class="feed-card-item"]/h2/a') # ʹ��xpath��ȡ����
        print(response) # ����Ӧ����Ӧ��״̬����200
        title_list = []
        for i in range(len(title)):
            title_list.append(title[i].get_text())
        item['title'] = title_list
        print(title)  # û����ȡ������
        yield item
