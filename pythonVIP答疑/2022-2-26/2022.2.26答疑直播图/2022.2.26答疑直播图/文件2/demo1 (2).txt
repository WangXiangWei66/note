# 江夏寄
# python学习
#用于爬取车站的代号
import requests
import re
import openpyxl
def get_station():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9226'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'
    stations=re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',resp.text)#这个正则表达式表示的是汉字和a到z的字母，其中|是或者的意思，\是转义字符
    #print(stations)
    #print(resp.text)#返回值是一个元组组成的那个的列表
    return stations
def save(lst):
    wb=openpyxl.Workbook()#创建一个工作簿对象
    ws=wb.active#创建一个活动的工作簿
    for item in lst:
        ws.append(item)#执行一次append，就会向工作表中去添加一行
    wb.save('station.xlsx')
if __name__ == '__main__':
    lst=get_station()
    save(lst)
