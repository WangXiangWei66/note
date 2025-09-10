# coding:utf-8
# author:杨淑娟

s='清明时节雨纷纷'
b=s.encode(encoding='utf-8')
print(b,type(b))  # str-->bytes
s2=bytes.decode(b)   # bytes-->str
print(s2)