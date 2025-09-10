import scrapy
from st.items import StItem
import os
import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

count = 1  # 初始值1
class StspSpider(scrapy.Spider): # 继承

    name = 'stsp'
    allowed_domains = ['699pic.com']
    start_urls = ['https://699pic.com/video-sousuo-0-18-0-0-0-1-4-popular-0-0-0-0-0-0.html']


    def parse(self, response):
        global count  # count就是全局变量
        count += 1     #
        print(response)
        # liList = response.xpath('//div[@class="video-list clearfix add-quick-recommend add-quick-recommend-b"]/ul/li')
                # print(liList)

        liList = response.xpath('//li')  # 数据提取，使用xpath
        # liList = liList[12:]
        # liList = response.css('div')
        print(len(liList))  # 测试性内容 ，打印输出一下列表的长度,li标签的个数
        # print(liList)
        # print(response.text)
        # //div[@class='video-list clearfix add-quick-recommend add-quick-recommend-b quick-recommend-show']/ul/li/a[2]/h3/text()

        newfolderName = 'page{}'.format(count)     # 格式化字符串  page2,  page3,page4....存储视频的文件夹的名称
        # 步骤二 创建一个新的文件夹
        if not os.path.exists(newfolderName):
            os.mkdir(newfolderName)  #如果文件夹不存在，则去创建

        for li in liList[10:-6]:   # 列表的切片操作 为什么是10：-6  打印输出liList查看
            video_link = li.xpath("./a/div/video/@data-original").extract_first()
            videoLink = 'https:' + video_link  #拼接完整路径
            title = li.xpath("./a[2]/h3/text()").extract_first()  # 视频的名称

            try:

                res = requests.get(videoLink,headers=headers) # 发送请求，向mp4的视频发送请求
                data = res.content  # 响应结果   （二进制)
                # videopath = newfolderName + '/' + title
                try:
                    with open(newfolderName + '/' + title + '.mp4','wb') as f:  # 存储视频
                        f.write(data)
                        print('%s下载成功'%title)
                except:
                    break
            except:
                break

            # print(videoLink,"--------",title)



            item = StItem(videoLink=videoLink,title=title)   # 创建对象
            yield item

            if count == 40:
                break
        next_url = 'https://699pic.com/video-sousuo-0-18-0-0-0-{}-4-popular-0-0-0-0-0-0.html'.format(count)
        # next_href = response.xpath("//ul[@class='pagination cls fl']/li[last()]/a/@href").extract_first()
        # if next_href:
        #     next_url = response.urljoin(next_href)
        request = scrapy.Request(next_url)
        yield request