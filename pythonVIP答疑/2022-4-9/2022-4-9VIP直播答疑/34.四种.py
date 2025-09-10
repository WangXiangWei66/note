# coding:utf-8
# author:杨淑娟
s=set() # 集合
s.update({'hello'}) # {}集合
print(s)
s.update(['python']) #['python']是列表
print(s)

#s.update(('world',)) #('world')为什么没有作为一个整体 添加进来
s.update(('world')) #没有加逗号是字符串类型
print(s)

s.update(('world',)) # 元组中只有一个元素后面也要加上逗号，否则认为是一个字符串，它执行的操作为 s.update('world')
print(s)
