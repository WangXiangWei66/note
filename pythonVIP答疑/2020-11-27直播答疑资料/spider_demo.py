# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
# 在Python中有一个第三方库叫requests,可以向服务器发送请求
import requests
from bs4 import  BeautifulSoup
url='https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'
# 使用User-Agent 伪装成浏览，防止反爬
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
resp=requests.get(url,headers=headers)
#print(resp.text)  #数据在HTML中可以使用BeautifulSoup解析

bs=BeautifulSoup(resp.text,'lxml')  #创建BS对象  lxml是html解释器
span_tag=bs.find_all('span',class_='pc_temp_num') #查找的是排名
#查找歌曲和歌手名称
a_tag_lst=bs.find_all('a',class_='pc_temp_songname')

#时长
span_time=bs.find_all('span',class_='pc_temp_time')  #以上三个列表的元素的个数相等

# 测试
# for item in span_time:
#     print(item)

for i in range(len(span_tag)):
    if i<3:  #列表中索引为0,1,2 ,排名中含有strong标签
        strong =span_tag[i].find('strong') # 获取到strong标签
        print(strong.text,a_tag_lst[i].text,span_time[i].text.strip())
    else:
        print(span_tag[i].text.strip(), a_tag_lst[i].text, span_time[i].text.strip())






