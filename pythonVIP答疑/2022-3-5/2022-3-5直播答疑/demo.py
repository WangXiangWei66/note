# coding:utf-8
# author:杨淑娟
import requests
from bs4 import BeautifulSoup
url='http://search.dangdang.com/?key=%C3%D7%D0%A1%C8%A6&act=input'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
resp=requests.get(url,headers=headers)
#print(resp.text)
bs=BeautifulSoup(resp.text,'lxml')
ul=bs.find_all('ul',class_='bigimg')
for item in ul:
    li=item.find_all('li' )
    for a in li:
        atag=a.find_all('a')
        for x in atag:
           if x.attrs.get('title')!=None:
               print(x['title'])
