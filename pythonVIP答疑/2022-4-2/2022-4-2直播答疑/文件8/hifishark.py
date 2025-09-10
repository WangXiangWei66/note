# 运城学院
# 张旭鹏
# 时间:2022/3/21 20:02
import openpyxl
import requests
import os
import time
import sys
from lxml import etree
from dingtalkchatbot.chatbot import DingtalkChatbot
keyword=input('请输入关键字:')
# Webkook=input('钉钉机器人的webhook链接:')
# interval_time=int(input('自定义更新频率:'))
def send_request():
    #url='http://hifishark.com/search?q='+keyword
    url='https://www.hifishark.com/search?q=kef+cresta'
    print(url)
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
    resp=requests.get(url,headers=headers)


    return resp.text
def parse_html(html):
    e=etree.HTML(html)
    product_name=e.xpath('//div[@class="search-product-info"]/span[@class="search-product-title"]/span/text()')
    price=e.xpath('//div[@class="search-product-info"]/span[@class="price"]/strong/text()')
    # print(len(product_name),len(price))
    lst=[]
    for i in range(len(price)):
        print(price[i])
    #     lst.append([product_name[i],price[i]])
    # print(lst)
    # return lst
def save(lst):
    wb=openpyxl.Workbook()
    sheet=wb.active
    for row in lst:
        # print(row)
        sheet.append(row)
    wb.save('hifishark.xlsx')
    # return
def judge_data(lst):
    wb=openpyxl.load_workbook('hifishark.xlsx')
    sheet=wb.active
    list=[]
    for i in sheet:
        row=[i[0].value,i[1].value]
        list.append(row)
    print(list==lst)
    return list==lst
    # print(sheet[1][0].value)
    # print(sheet[1][1].value)
    # print(list([sheet[1][0].value,sheet[1][1].value]))
def send_update():
    webhook=Webkook
    ddrobot=DingtalkChatbot(webhook)
    ddrobot.send_text(msg=f'您所关注的产品{keyword}更新通知')
def Spider():
    result=send_request()
    # print(result)
    parse_html(result)
    lst=parse_html(result)
    # save(lst)
    # return lst
def start():
    Spider()
    # while True:
    #     time.sleep(interval_time)
    #     lst=Spider()
    #     if not judge_data(lst):
    #         os.remove('hifishark.xlsx')
    #         save(lst)
            # send_update()
if __name__ == '__main__':
    start()
    # judge_data()
