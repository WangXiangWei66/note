# coding:utf-8
# author:杨淑娟
d={'a':1,'b':2,'c':3}
d2={'d':4,'e':5,'c':8}

#删除字典的元素使用del 语句
del  d['a']
print(d)

# 合并字典使用update
d.update(d2)   # 键相同时，值进行覆盖
print(d)
