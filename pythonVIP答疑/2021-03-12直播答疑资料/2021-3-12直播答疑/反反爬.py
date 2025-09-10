# 教育机构：马士兵教育
# 讲    师：杨淑娟
import requests
url='https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date=2021-03-19&leftTicketDTO.from_station=CCT&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E9%95%BF%E6%98%A5,CCT&ts=%E9%95%BF%E6%B2%99,CSQ&date=2021-03-19&flag=N,N,Y'
,'cookie':'JSESSIONID=5839BAF96133961F7FB538AA3938842E'
}
#发送请求
resp=requests.get(url,headers=headers)
print(resp.text)