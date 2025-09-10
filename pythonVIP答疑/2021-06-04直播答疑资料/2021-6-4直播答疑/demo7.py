#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%A9%AC%E5%A3%AB%E5%85%B5&fenlei=256&rsv_pq=83fc85be00091a60&rsv_t=0712UEnICkV%2Bu9EezTrETd6SFmJuJEhvuXYP03zrRsljRXxH%2FhR4aUGCSA0&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=4&rsv_sug1=4&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=%25E9%25A9%25AC%25E5%25A3%25AB%25E5%2585%25B5&rsp=5&inputT=4422&rsv_sug4=6571

#url中的中文为什么要编码？
import urllib.parse
s='%E9%A9%AC%E5%A3%AB%E5%85%B5'
# 解码
s2=urllib.parse.unquote(s)
print(s2) #马士兵

# url中的中文的编码
s=urllib.parse.quote(s2)
print(s) # %E9%A9%AC%E5%A3%AB%E5%85%B5
#       将str与bytes之间进行转换，目的是网络传输数据
print('---------------encode 与decode -------------')
s='马士兵'
print(s.encode('utf-8')) # utf-8, 一个中文占三个字节
print(s.encode('gbk')) # gbk, 一个中文占两个字节

# 解码bytes的方法
ss=b'\xe9\xa9\xac\xe5\xa3\xab\xe5\x85\xb5'
print(bytes.decode(ss))