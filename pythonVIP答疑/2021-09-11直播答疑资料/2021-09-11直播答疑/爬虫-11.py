# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import requests
import json
url='https://api2.paixin.com/albums/170/medias?page=0&size=45&sort=createdAt,desc'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
resp=requests.get(url,headers=headers)
data=json.loads(resp.text)
#解析数据
lst=data['elements'] # 字典取值，结果为列表
image_urls=[] # 存储所有图片的url
for item in lst:
    img_url=item['image'] # 字典取值 ，结果为str， 图片的Url
    image_urls.append('http:'+img_url) # 拼接成下确的url

#分别向每一个图片的url发送请求，下载图片
count=1
for item in image_urls:
    resp_image=requests.get(item,headers=headers) # 图片的响应结果是二进制数
    #保存到本地
    with open('image/'+str(count)+'.jpg','wb') as file : #ｗｂ表示写入二进制数
        file.write(resp_image.content) #响应的ｃｏｎｔｅｎｔ表示的是二进制数
    count+=1
    print(count,'下载成功')


