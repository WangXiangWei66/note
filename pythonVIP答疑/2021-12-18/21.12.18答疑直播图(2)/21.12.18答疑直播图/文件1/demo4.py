"""爬百度贴吧"""

import os
import requests
import re
import time
import random
print(os.getcwd())
class TiebaSpider:
    """贴吧爬虫"""

    def __init__(self):
        """初始化参数"""
        self.kw = input('关键词>')
        self.base_url = 'http://tieba.baidu.com/f'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
        self.page_num = 1
        self.title = ''

    def parse_text(self, url, params=None):
        """发送请求，获取响应内容"""

        # 休眠，避免被对方反爬检测到
        time.sleep(random.randint(1, 5))

        req = requests.get(url, headers=self.headers, params=params)
        return req.text

    def parse_byte(self, url, params=None):
        """发送请求，获取响应内容"""

        time.sleep(random.random() * 2)
        req = requests.get(url, headers=self.headers, params=params)
        return req.content

    def page(self, content):
        """解析每一页"""

        print('第{}页爬取中...'.format(self.page_num))
        self.page_num += 1

        url_title = re.findall(r'<a rel="noreferrer" href="(/p/\d+?)" title=".+?" target="_blank" class="j_th_tit ">(.+?)</a>', content)
        #print(url_title)
        for url, title in url_title:
            self.title = title
            self.detail('https://tieba.baidu.com' + url)

            # 保存标题
            self.save_title()

        # 判断下一页
        next_url = re.findall(r'<a href="(.*?)" .*?>下一页&gt;</a>', content)
        if next_url:
            next_url = 'https:' + next_url[0]
            content = self.parse_text(url=next_url)
            self.page(content)
        else:
            print('爬虫结束...')

    def detail(self, url):
        """每一个帖子的详情"""
        content = self.parse_text(url=url)
        urls = re.findall(r'<img class="BDE_Image".*?src="(.*?)".*?>', content)
        for url in urls:
            self.save_img(url=url)

    def save_title(self):
        """保存帖子的标题"""
        with open('./data/tieba/tieba_{}.txt'.format(self.kw), 'a', encoding='utf-8') as file:
            file.write(self.title)
            file.write('\n')

    def save_img(self, url):
        """保存图片"""
        content = self.parse_byte(url=url)
        dirpath = "data/tieba/images"
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        image_path = './data/tieba/images/{}_{}'.format(self.title, str(url[url.rfind('/') + 1:]).replace(':','').replace('。',''))
        with open(image_path, 'wb') as file:
            file.write(content)

    def start(self):
        """开始爬虫"""
        print('爬虫开始...')
        content = self.parse_text(url=self.base_url, params={'kw': self.kw, 'ie': 'utf-8', 'fr': 'search'})
        self.page(content)


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.start()
