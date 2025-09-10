# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
from urllib import request
import re
from bs4 import BeautifulSoup
#       http://music.163.com/discover/toplist?id=3778678
url = 'http://music.163.com/discover/toplist?id=3778678'
html = request.urlopen(url).read().decode('utf-8')
# \s 匹配任意空白字符，\d 匹配任意十进数 ｛1，20｝1到20次 .任意字符，  +匹配前一个字符1到多次 ？匹配前一个元字符0到1次

dataList = re.findall("<a\shref=.+?song.id=\d{1,20}.+?>.+?<.a>",html) # 获取所有匹配的内容

num = 1

for data in dataList:
    bs = BeautifulSoup(data,'html.parser')
    a_tag=bs.find('a')
    print(str(num) + "   " +a_tag.text)
    num += 1


