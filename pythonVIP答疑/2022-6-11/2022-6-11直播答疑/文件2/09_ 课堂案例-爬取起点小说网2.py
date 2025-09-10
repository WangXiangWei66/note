# _*_ coding: UTF-8 _*_
# 2022/6/6 20:17
import requests
from bs4 import BeautifulSoup

url = 'https://www.qidian.com/all/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

resp = requests.get(url,headers=headers)
bs=BeautifulSoup(resp.text,'lxml')

h2_tag=bs.find_all('div',class_='book-mid-info')
title=[]
for item in h2_tag:
    h2=item.find('h2')
    #print(h2.text)
    title.append(h2.text)

# 作者
p_tag=bs.find_all('p',class_='author')
author=[]
for item in p_tag:
    a=item.find('a')
    #print(a.text)
    author.append(a.text)
total=[]
for x,y in zip(title,author):
    total.append((x,y))
print(total)