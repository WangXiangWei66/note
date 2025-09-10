# _*_ coding: UTF-8 _*_
# 2022/6/6 20:17
import requests
from pyquery import PyQuery  # 用于解析数据

url = 'https://www.qidian.com/all/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

resp = requests.get(url,headers=headers)
# print(resp.text)
# 初始化PyQuery对象
doc = PyQuery(resp.text)
# a_tah = doc('h2 a')
# print(a_tah)

print('-------第一种：讲义代码：--------')
names = [a.text for a in doc('h2 a')] # 书名
authors= doc('p.author a')
author_lst = []
for index in range(len(authors)):
    if index%3==0 or index==0:
        author_lst.append(authors[index].text)
for name,author in zip(names,author_lst):
    print({name: author})



print('-------第二种：延伸思路-----------')
names = [a.text for a in doc('h2 a')] # 书名
# print(names)
authors= [b.text for b in doc('h2').siblings('p.author a.name')] # 作者
# print(authors)
for name,author in zip(names,authors):
    print({name: author})