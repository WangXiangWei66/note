# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 8:05准时开始

import  requests  # 导入爬虫的第三方库  （事先进行安装 pip install requests）
import json
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
d={'长沙':'101250101','北京':'101010100','上海':'101020100'}
loc=input('请输入城市名称:')
url=f'https://devapi.qweather.com/v7/weather/now?key=9a8fc16bb3884a668fa48f9106969c44&location={d.get(loc)}'
resp=requests.get(url,headers=headers)  # 为什么使用get，因为API告诉我的是 GET请求
#print(resp.text)
json_data=json.loads(resp.text)
newkey=json_data['now']
temp=newkey['temp'] # 温度
text=newkey['text'] #文本
feelslike=newkey['feelsLike'] # 体感温度
print('城市名称:',loc)
print('温度:',temp)
print('天气:',text)
print('体感温度:',feelslike)






