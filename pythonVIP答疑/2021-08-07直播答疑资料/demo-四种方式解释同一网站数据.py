#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import requests
import sys,io
import re
from lxml import etree
from  bs4 import BeautifulSoup
from pyquery import PyQuery
url='https://www.meishij.net/chufang/diy/?page=1'
# 添加请求头，目的是防止反扒
# UA只与浏览器有关，与网站无站
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
# 因为该网站的数据都是在HTML中，所以可以使用四种方式去提取
# 爬取数据的函数
def get_html(url):
    resp=requests.get(url,headers=headers)
    # 解决乱码问题
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
    return resp.text

#第一种解析数据的方式  正则
def re_test(html):
    result=re.findall('<img class="img" alt="(.*)" src="(.*)">',html)
    print(result)

# 第二种解析数据的方式--xpath
def xpath_test(html):
    root=etree.HTML(html)
    names=root.xpath('//img[@class="img"]/@alt')
    src_lst=root.xpath('//img[@class="img"]/@src')
    # 这个for循环有不懂的吗？
    for name,src in zip(names,src_lst):
        print(name,src)

#第三种解析数据的方式bs
def bs_test(html):
    bs=BeautifulSoup(html,'lxml')
    img_lst=bs.find_all('img',class_='img')
    for img in img_lst:
        name=img['alt']
        src=img['src']
        print(name,src)


# 第四种解析数据的方式-pyquery
def pyquery_test(html):
    doc=PyQuery(html) #创建PyQuery的对象 ,
    img_lst=doc('div a').find('img.img').items() # img是标签  .img是类样式
    for item in img_lst:
        print(item.attr('alt'),item.attr('src'))

#测试
#print(get_html(url))

pyquery_test(get_html(url)) # 将爬虫取的响应结果作为参数传给解析的函数