# -*- coding:utf-8 -*-
import os
import requests
import json
from urllib import request
url = "https://image.so.com/j?q=%E5%A3%81%E7%BA%B8%E7%8C%AB%E5%92%8C%E8%80%81%E9%BC%A0%27"
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 QIHU 360SE/12.2.1940.0', 'Referer': 'https://image.so.com'}
response = requests.get(url, headers = headers).text
results = json.loads(response)
rawdata = results['list']  # rawdata是一个列表，这个列表中的每个元素都是一个字典
# print(rawdata)
if not os.path.exists('img'):
    os.mkdir('img') # 如果在当前文件夹下不存在img文件夹，将新建一个

for item in rawdata: # 遍历列表
    img_url = item['img']
    title=item['title'].replace('<em>','').replace('</em>','').replace('?','').replace('|','')
    print(title)
    request.urlretrieve(img_url, os.path.join( 'img/' + f'{title}'+'.jpg'))