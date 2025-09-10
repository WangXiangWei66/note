# coding:utf-8
# author:杨淑娟
import urllib.parse
kw={'wd':'马士兵'}
#解码
result=urllib.parse.urlencode(kw)
print(result)
result.read() # 没有这个属性怎么看源码啊
