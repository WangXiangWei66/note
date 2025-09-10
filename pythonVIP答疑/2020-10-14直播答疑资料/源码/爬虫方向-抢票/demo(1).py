#教育机构 ：马士兵教育
#讲    师：杨淑娟
#用于爬取车站代号
import  requests
import  re
import  openpyxl
def get_station():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9151'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'
    #print(resp.text)
    stations=re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',resp.text)
    #print(stations)
    return  stations #stations是一个列表

def save(lst):
    wb=openpyxl.Workbook() #创建工作薄对象
    ws=wb.active #使用活动表
    for item in lst:
        ws.append(item)  #每执行一次append将向sheet中添加一行
    wb.save('车站代码.xlsx')

if __name__ == '__main__':
    lst=get_station()
    save(lst)
