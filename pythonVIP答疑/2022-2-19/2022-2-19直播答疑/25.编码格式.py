# coding:utf-8
# author:杨淑娟

s='北京冬奥的开幕式很好看'
b=s.encode('utf-8') # 字符串的编码
print(b,type(b))

# 解码
s2=bytes.decode(b,encoding='utf-8')
print(s2,type(s2))