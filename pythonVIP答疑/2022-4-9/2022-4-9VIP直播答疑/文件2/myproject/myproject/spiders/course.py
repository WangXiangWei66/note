import scrapy


class CourseSpider(scrapy.Spider):
    name = 'course'
    # allowed_domains = ['icourse163.org']
    start_urls = ['https://www.icourse163.org/channel/3002.htm?cate=-1&subCate=-1']

    def parse(self, response):
        div_list=response.xpath('//div[@class="Y8tgZ"]/div[1]')
        print(div_list)
        for div in div_list:
            title=div.xpath('./h3/text()').extract
            author=div.xpath('./div/text()').extrat
            people=div.xpath('./span//text()').extract
            print(title,author,people)
            yield {
                "title":title,
                "author":author,
                "people":people,
            }
