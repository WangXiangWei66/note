# coding:utf-8
# author:杨淑娟
import requests
proxy = '113.194.28.190:9999'

proxies = {
	        'http': 'http://' + proxy,
	        'https': 'https://' + proxy
		  }
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
