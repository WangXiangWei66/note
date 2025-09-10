# coding:utf-8
# author:杨淑娟

lst=[10,20,30,40,50,10,20,30,40]
print(lst.pop()) # 从列表的尾部开始删除
lst.remove(10) # 删除重复元素的第一个
print(lst)

del lst[0] # 删除列表中索引为0的元素
print(lst)

lst.clear() # 删除列表中所有元素
print(lst)