# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
from urllib import  request  # request是Python内置的模块
import  re   # 导入正则表达式的模块
from bs4 import  BeautifulSoup

url='http://music.163.com/discover/toplist?id=3778678'


html=request.urlopen(url).read().decode('utf-8')  #html就是一个响应结果

#对响应结果进行提取数据
#常用的数据解析方式 ：正则表达式，Xpath，PyQuery，BeautifulSoup

#\s匹配任意空白字符

datalst=re.findall("<a\shref=.+?song.id=\d{1,20}.+?>.+?<.a>",html)
#print(datalst)

for item in datalst:
    bs=BeautifulSoup(item,'html.parser')
    a_tag=bs.find('a')
    print(a_tag.text) # a标签中的文本
