# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import requests
def get_request():
    url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2021-09-12&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=TJP&purpose_codes=ADULT'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
             'Cookie': 'JSESSIONID=3FC9CD0D27F37BD90044B6AB7C35BE53; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_wfdc_flag=dc; RAIL_EXPIRATION=1588656485140; RAIL_DEVICEID=lrPFTJvtsqw-g3Mn7Z3Zfm7_6Mr1iFGqDnOY5aNh88kU4v4kIzfdfTEypjzG9-BNwhEIXiyWL85qDmsFhq5vJUgS26ReAcfysH5jTm3Mx17LWHZRxj0eN8_eiIBsiiKYx39pTI6s5LHe83cECSwIwzHiXIK3UPnA; _jc_save_fromDate=2020-05-06; _jc_save_toStation=%u5929%u6D25%2CTJP; BIGipServerpassport=770179338.50215.0000; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=1507393802.64545.0000; _jc_save_toDate=2021-09-12'}
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8-sig'
    return resp
def parse_html(resp):
    json_ticket=resp.json()
    data_lst=json_ticket['data']['result']
    for item in data_lst:
         d=item.split('|')
         print(d[3],d[6],d[7],d[31],d[30],d[13])  #3为车次 6为始发站，7为终点站
def start():
    parse_html(get_request())
if __name__ == '__main__':
    start()