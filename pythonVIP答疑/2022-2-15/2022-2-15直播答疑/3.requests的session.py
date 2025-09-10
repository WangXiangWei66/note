# coding:utf-8
# author:杨淑娟
import  requests
#创建session对象
s=requests.Session() # 创建一个Session对象  （代表的是一个用户）
# 使用这个session对象发送请求
resp=s.get('http://httpbin.org/cookies/set/pwd/1234') # 发送请求同时设置一个一cookie信息
print(resp.text)

# 使用同一个session再次发送请求
resp2=s.get('http://httpbin.org/cookies')
print(resp2.text)

# 为了验证不同的session对象，   代表不同的用户
s2=requests.Session()  #创建的第二个Session对象
resp3=s2.get('http://httpbin.org/cookies')
print(resp3.text)