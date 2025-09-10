# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 爬取起点小说网
import requests
from lxml import etree
url='https://www.qidian.com/rank/yuepiao?style=1'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'} # 添加请求头，防止反爬
resp=requests.get(url,headers=headers)
e=etree.HTML(resp.text) # 要解释的文本是resp.text
story_names=e.xpath('//div[@class="book-mid-info"]/h4/a/text()')
authors=e.xpath('//p[@class="author"]/a[1]/text()')
#名称
#  作者
#print(story_names)
#print(authors)
# 怎么将两个列表合成一个列表呢，使用内置的函数zip,将列表中的数据打包
lst=[]
for name,a in zip(story_names,authors):
    lst.append({name:a}) # ｛｝自己定义的字典

for item in lst:
    print(item)
