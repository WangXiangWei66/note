# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 爬虫
import requests
import json
url='https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=2379852&count=10&page=0&filter_rating=0&bkn=823873011&r=0.1725389475564436'
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
'referer': 'https://ke.qq.com/course/2379852'
}

resp=requests.get(url,headers=headers)
#print(resp.text)
json_data=json.loads(resp.text)
lst=json_data['result']['items'] # 列表 中存储的是N 个字典
for item in lst:
    print(item['first_comment']) #iteｍ是一个字典



