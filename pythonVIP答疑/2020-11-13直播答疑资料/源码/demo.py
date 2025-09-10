# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
# 爬虫--》反爬虫的处理
import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}
resp=requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=25694775368&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
                  headers=headers)
print(resp.text)
print(resp) #<Response [200]>
print(resp.request.headers) #'python-requests/2.24.0'

