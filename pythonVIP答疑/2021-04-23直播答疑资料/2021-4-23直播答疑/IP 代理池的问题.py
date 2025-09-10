# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 为什么要使用IP代理池？对网站的爬取速度过快，或次数过多的时候，容易被封IP
# 使用“他人”IP访问服务器，这个他人的IP定期更换， 咱们体验课的IP一秒钟换一次

# 比特代理
import requests
import  random


# 使用爬虫爬虫IP：
# resp=requests.get('http://47.105.97.33/Index-generate_api_url.html?packid=2&fa=0&qty=20&port=1&format=txt&ss=1&css=&pro=&city=&usertype=9')
# # with open('b.txt','a+') as file:
# #     file.write(resp.text)

# 从文件中读取IP地址
with open('b.txt','r')as file:
    s=file.read()

#使用换行将字符串分割成列表
lst=s.split('\n\n')
#print(lst)
url='http://www.baidu.com'
#
# # 定义代理IP  （如果有的IP不能用怎么办，使用try-except）
for i in range(3):
    proxie={
        'http':'http://'+random.choice(lst)
    }
    print(proxie['http']) # 发送请求的ip地址
    # 使用代理IP发送请求
    resp=requests.get(url,proxies=proxie)
    resp.encoding=resp.apparent_encoding # 解决响应乱码问题
    print(f'第{i+1}次访问百度')
    print(resp.text)


