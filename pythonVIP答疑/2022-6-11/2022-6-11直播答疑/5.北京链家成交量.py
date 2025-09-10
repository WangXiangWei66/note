# coding:utf-8
# author:杨淑娟
import requests
import io,sys
from bs4 import BeautifulSoup
url='https://bj.lianjia.com/ershoufang/'   # 请求的UrL
# 为什么要使用headers啊？其实就是反反爬
headers={
'Cookie': 'lianjia_uuid=b5a8a48d-f73b-43a4-983f-99c4870f7afa; UM_distinctid=17ee7bd9e00277-02812bd0a091dc-3e644204-1bcab9-17ee7bd9e01d3e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ee7bd9ef1266-047a7a00479167-3e644204-1821369-17ee7bd9ef2e63%22%2C%22%24device_id%22%3A%2217ee7bd9ef1266-047a7a00479167-3e644204-1821369-17ee7bd9ef2e63%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.1378332734.1644565474; _smt_uid=620613e5.1f76779b; CNZZDATA1253477573=438288882-1644558936-%7C1644900549; CNZZDATA1254525948=976226423-1644555831-%7C1644901434; CNZZDATA1255633284=108812519-1644561727-%7C1644897400; CNZZDATA1255604082=2055206748-1644557259-%7C1644902872; _jzqx=1.1653623246.1653623246.1.jzqsr=tj%2Elianjia%2Ecom|jzqct=/ershoufang/c1220039349603132/.-; select_city=110000; lianjia_ssid=1522857a-f4a8-4f17-989b-85002756641b; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1653621264,1654063361,1654929810; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1654929810; _jzqa=1.2154745539045989600.1653621249.1654063348.1654929810.4; _jzqc=1; _jzqckmp=1; _qzja=1.747446422.1653621249498.1653621249498.1654929810013.1653621249498.1654929810013.0.0.0.2.2; _qzjc=1; _qzjto=1.1.0; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMzZlY2IzMGEzZGIyYzczMzdlMDU5NjJmM2I2ODNhNTNiODIzOTlmMTIwMjlkNTczMjM5NDYxMDE4YjdlZDYzMDcyNmZlMDU3ZmEwY2JkZmRkM2FhMWZhYTI2MDM1ZmFhMDllODMwMDg3NDM0MmNkYjk2ZDcwZDcwYzg2ZDIxMzExNjZkODM4MWYyY2FkMDQ1ZWM3MDUzZWIwMGNhNDdiZjJhY2E0ZTU1ODllYzA2Y2U4MWEwZjEzZWZjZWE0ZGMwNjU3NjJlNzU5OGUzMjU5OGJkY2Q3NDZhOTMyM2NlYmMxOGEwMWIyYmViY2RlMWI5MjM1YjRhZTMyZWJiNDMxZVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI3Yzk0OGQwMVwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _jzqb=1.1.10.1654929810.1; _qzjb=1.1654929810012.1.0.0.0; _gid=GA1.2.236758666.1654929814',
  'host':  'bj.lianjia.com'
}

# 处理爬虫响应结果乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='GB18030')

resp=requests.get(url,headers=headers)  # 发送请求--->获取一个响应结果

#print(resp.text)

bs=BeautifulSoup(resp.text,'lxml')         # 解析提取响应数据

div_tag=bs.find_all('div',class_='title')  # 提取出所有的类样式为title的div元素

title_list=[]
for item in div_tag[:len(div_tag)-7]:
    #print(item.text)
    title_list.append(item.text)

span_tag=bs.find_all('div',class_='positionInfo') # 提取所有类样式为positionInfo的div元素
position_lst=[]
for item in span_tag:
   a_tag=item.find('a')  # 从div中再提取a标签（只提取第一个a标签）
  # print(a_tag.text)
   position_lst.append(a_tag.text)
total=[]
  # zip函数的作用，是对列表，元素等元素进行“打包” ,打包结果是一个元组,
for x,y in zip(title_list,position_lst):
    total.append((x,y))
#
for item in total:
    print(item)

