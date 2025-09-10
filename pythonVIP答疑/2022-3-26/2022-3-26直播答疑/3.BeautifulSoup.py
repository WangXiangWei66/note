# coding:utf-8
# author:杨淑娟
# 掌握 find

from bs4 import  BeautifulSoup
bs=BeautifulSoup('<html><head></head><body><h1 class="bg">helloworld</h1><h1>hello</h1></body></html>','lxml')
h1tag=bs.find_all('h1',class_='bg') # 查询所有的h1 ,h1标签的列表
#print(h1tag)
for item in h1tag:
    print(item.text)  # 获取标签中的内容
