import requests
from pymysql import *
from lxml import etree
import re


class LinJiaSpider():
    # 创建数据库连接
    conn = connect(host='localhost', port=3306, user='root', password='root', db='Mytest1', charset='utf8')
    # 打开游标
    cur = conn.cursor()

    def __init__(self):
        self.page = [i for i in range(4)]
        self.url = 'https://wx.fang.lianjia.com/loupan/pg{0}/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
        self.names_list = []
        self.type_list = []
        self.status_list = []
        self.region_list = []
        self.locations_list = []
        self.price_list = []
        self.areas_list = []
        self.avg_price_list = []

    def send_request(self,url):
        resp = requests.get(url,headers=self.headers)
        if resp.status_code == 200:
            return resp


    def parse_html(self,resp):
        html = resp.text
        soup = etree.HTML(html)
        lst = []

        hnames = soup.xpath("//div[@class='resblock-name']/a/text()")
        types = soup.xpath("//span[@class='resblock-type']/text()")
        hstatus = soup.xpath("//span[@class='sale-status']/text()")
        region = soup.xpath("//div[@class='resblock-location']/span/text()")
        locations = soup.xpath("//div[@class='resblock-location']/a/text()")
        # designs = soup.xpath("//a[@class='resblock-room']/span/text()")
        areas = soup.xpath("//div[@class='resblock-area']/span/text()")
        avg_price_lst = soup.xpath("//span[@class='number']/text()")
        avg_price_list = []
        for avg_price in avg_price_lst:
            avg_price += '元/平方米（均价）'
            avg_price_list.append(avg_price)
        prices = soup.xpath("//div[@class='second']/text()")

        '''
        # 这个i 会超过列表长度 第一页之后就会超出range了,并且i也不能从0开始遍历 是从最后开始遍历的

        for i in range(len(hnames)):
            lst.append((hnames[i],types[i],hstatus[i],region[i],locations[i],areas[i],avg_price_list[i],prices[i]))
        print(lst)

        # page = re.match('^pg\d*$',full_url)
        # print(page)
        '''


        # 这里怎么拿到最后一个lst的最后一个列表呢
        for hname, type, hstatus, region, location, area, avg_price,price in zip(hnames, types, hstatus, region, locations, areas,avg_price_list,prices):
            self.names_list.append(hname)
            self.type_list.append(type)
            self.status_list.append(hstatus)
            self.region_list.append(region)
            self.locations_list.append(location)
            self.areas_list.append(area)
            self.avg_price_list.append(avg_price)
            self.price_list.append(price)

        for i in range(len(self.names_list)):
            lst.append((self.names_list[i],self.type_list[i],self.status_list[i],self.region_list[i],
                       self.locations_list[i],self.areas_list[i],self.avg_price_list[i],self.price_list[i]))
        lst2 = []
        for i in lst:
            lst2.append(i)
        print(lst2)


        # for i in range(len(hnames)):
        #     lst.append((self.names_list[i], self.type_list[i], self.status_list[i],  self.region_list[i],  self.locations_list[i],
        #                 self.areas_list[i],  self.avg_price_list[i], self.price_list[i]))


        # for hname,type in zip(hnames,types):
        #     self.names_list.append(hname)
        #     self.type_list.append(type)
        # print(self.names_list,self.type_list)

        # print(lst)
        # self.save(lst)

    def save(self,lst):
        # print(self.conn)
        # print(lst)
        sql = "insert into tb_lianjia  values(%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cur.executemany(sql,lst)
        self.conn.commit()
        print(self.cur.rowcount,'数据插入完毕.')


    def start(self):
        for i in range(1,len(self.page)):
            full_url = self.url.format(i)
            resp = self.send_request(full_url)
            # print(resp.text)
            self.parse_html(resp)
        # global full_url


if __name__ == '__main__':
    lianjia = LinJiaSpider()
    lianjia.start()

