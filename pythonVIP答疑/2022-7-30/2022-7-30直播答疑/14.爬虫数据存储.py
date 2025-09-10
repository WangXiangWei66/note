# coding:utf-8
# author:杨淑娟
import requests
from bs4 import BeautifulSoup
# 数据的爬取
url='https://www.qidian.com/rank/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
resp=requests.get(url,headers=headers)
lst=[]
bs=BeautifulSoup(resp.text,'lxml')
div=bs.find('div',class_='book-list')
ul=div.find('ul')
lilst=ul.find_all('li')
for item in lilst:
    atag=item.find('a')
    if atag!=None:
        lst.append(atag.text)
print(lst)  # 将爬取的数据存到lst列表中


# 数据存储
import json
import pandas as pd   #
# 定义了一个函数， 存到Excel文件中的
def save_excel(lst):
    df=pd.DataFrame(data=lst)
    df.to_excel('a.xlsx')

def save_csv(lst):
    df = pd.DataFrame(data=lst)
    df.to_csv('b.csv',index=False)

def save_json(lst):
    json.dump(lst,open('c.json','w'),ensure_ascii=False)

if __name__ == '__main__':
    save_excel(lst)   # 结果保存到excel中
    save_csv(lst)  # 结果保存到csv中
    save_json(lst)  # 结果写到文件中，json格式