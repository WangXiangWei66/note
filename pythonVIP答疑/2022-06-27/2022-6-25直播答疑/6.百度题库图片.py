# coding:utf-8
# author:杨淑娟
import requests,json,re
url='https://tiku.baidu.com/bigque/interface/getqueinfos?action=getquebykp&format=jsonp&kp_id=32b249649b6648d7c1c74667&start=1&rn=5&kp_type=knowpoint&_=1656084646167'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
         }
resp=requests.get(url,headers=headers)

x=resp.json()
print(x)

ddd=u'\u57ce'
ddd=ddd.encode("gb18030").decode("gb18030")
print(ddd)
