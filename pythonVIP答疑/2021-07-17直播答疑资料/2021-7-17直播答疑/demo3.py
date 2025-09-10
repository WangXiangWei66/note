#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 分清真假URL
import requests
from lxml import  etree
import re
import sys,io
url='http://www.mca.gov.cn/article/sj/xzqh/2019/'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
# 向主页发送请求
resp=requests.get(url,headers=headers)

# 解决响应结果页面编码问题
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# 使用xpath提取 ，提取 a class="artitlelist"
html=resp.text
parse_html=etree.HTML(html)
a_list=parse_html.xpath('//a[@class="artitlelist"]')

for a in a_list:
    title=a.get('title')

    if title.endswith('代码'): # 获取的title标签中的文本以代码结尾的文本
        # 获取href  (这是一个假的链接)
       false_link= 'http://www.mca.gov.cn'+a.get('href')
       print(false_link)
       # 向假链接发送请求
       resp2=requests.get(false_link,headers=headers)
      # print(resp2.text) # 响应结果中没有想要的数据，就可以是一个假的url
        # 真正的url是通过JS发送的
        # 获取JS中真正的url
       re_dbs=r'window.location.href="(.*?)"'
       pattern=re.compile(re_dbs) # 构建正则规则对象
       true_link=pattern.findall(resp2.text)[0] # findall的结果是列表，只要列表中的第一项
       # 向真正的url发送请求
       resp3=requests.get(true_link,headers=headers)
      # 提取数据
       parse_html=etree.HTML(resp3.text)
       tr_lst=parse_html.xpath('//tr[@height="19"]')
       # 提取出来的结果是一个列表
       for tr in tr_lst:
          code=tr.xpath('./td[2]/text()')
          name = tr.xpath('./td[3]/text()')
          print(code,name)
       break