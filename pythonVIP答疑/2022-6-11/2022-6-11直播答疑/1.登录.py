# coding:utf-8
# author:杨淑娟

import requests
url='http://127.0.0.1:8000/admin/'
resp=requests.post(url,data={'username':'admin','password':'admin123'})
print(resp.status_code) # 403 网站反爬处理

import requests
url='http://127.0.0.1:8000/login_action/'
resp=requests.post(url,data={'username':'admin','password':'admin123'})
print(resp.status_code) # 登录成功的 200 OK
