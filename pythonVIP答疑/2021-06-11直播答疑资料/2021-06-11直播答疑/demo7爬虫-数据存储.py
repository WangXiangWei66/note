#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import requests
from  bs4 import BeautifulSoup
import openpyxl
url='http://www.csres.com/notice/50655.html'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
# 发送请求的函数
def send_requests():
    resp=requests.get(url,headers=headers)
    return resp.text

# 解析数据
def parse(html):
    bs=BeautifulSoup(html,'lxml') #lxml是解析器，html.parser
    # 获取到了含有数据的表格
    table=bs.find('table',id='table1')
    #print(table)
    trs=table.find_all('tr')
    lst=[] # 用于存储数据
    for item in trs: # 遍历所有的行
        tds =item.find_all('td') # 从tr中获取所有的td
        sub_lst=[] # 存储每一列数据
        for td in tds: # 遍历td
           sub_lst.append(td.text.replace('\t','').replace('\n','').replace('\r','').replace('\u3000',''))
        lst.append(sub_lst)
    return lst
# 存储
def save(lst):
    wk=openpyxl.Workbook() # 创建工作簿
    sheet=wk.active # 获取工作表
    # 向工作表中添加数据
    for item in lst:
        sheet.append(item)
    wk.save('aaa.xlsx')
# 以主函数的方法运行
if __name__ == '__main__':
   save( parse(send_requests()))