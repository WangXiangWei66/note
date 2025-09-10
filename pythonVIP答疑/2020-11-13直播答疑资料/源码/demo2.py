# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
         'Cookie': '_uab_collina=159430816448986374678579; JSESSIONID=1457E6C8C32F51302366554446581A15; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u5E7F%u5DDE%u5357%2CIZQ; _jc_save_toStation=%u90D1%u5DDE%2CZZF; RAIL_EXPIRATION=1605425865445; RAIL_DEVICEID=pS2abwbv0PX5GqzK0OD2lKQldqoV35vsDgbZGLKmVQg1o1aJj2QyiC9XrChWV-01UfpJ-ilP5tbldDLx6otaqVqmeQwiC7fA4AeKhXpnj4P5tKiA42mtBsezeGX6cdp3gC2HZFBS92eePiRPQyKDYHnfkJ4Hj4W7; _jc_save_toDate=2020-11-13; BIGipServerotn=468713994.64545.0000; BIGipServerpool_passport=283378186.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_fromDate=2020-11-16'}
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-11-16&leftTicketDTO.from_station=IZQ&leftTicketDTO.to_station=ZZF&purpose_codes=ADULT'
resp=requests.get(url,headers=headers)
print(resp.text)
