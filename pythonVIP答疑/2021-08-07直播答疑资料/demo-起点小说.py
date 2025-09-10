#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

from pyquery import  PyQuery as pq
import  requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
url='https://www.qidian.com/rank/yuepiao?style=1'
resp=requests.get(url,headers=headers)
doc=pq(resp.text)
names=[a.text for a in doc('h4 a')]
authors=doc('p.author a')
author_list=[]
for index in range(len(authors)):
    if index%2==0:
        author_list.append(authors[index].text)
#print(names)
#print(author_list)
for name,author in zip(names,author_list):
    print(name, ':',author)