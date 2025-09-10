# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import  requests  #第三方模块
from bs4 import BeautifulSoup #解析提取数据
url='https://175dt.com/17'
# 发送请求，获取响应结果
resp=requests.get(url)
#print(resp.text)
bs=BeautifulSoup(resp.text,'lxml')
h2tag=bs.find_all('h2') #提取所有的h2标签  ,结果为列表
for h2 in h2tag:
    print(h2.text)

ptag=bs.find_all('p')  #提取所有的p标签，结果为列表
for p in ptag:
    print(p.text.strip())