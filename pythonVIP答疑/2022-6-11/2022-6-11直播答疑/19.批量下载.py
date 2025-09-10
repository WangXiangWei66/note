# coding:utf-8
# author:杨淑娟
import requests
url='https://c.wallhere.com/photos/b6/34/'
resp=requests.get(url)
print(resp.text)
