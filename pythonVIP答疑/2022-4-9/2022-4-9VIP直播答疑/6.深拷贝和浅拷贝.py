# coding:utf-8
# author:杨淑娟
import  copy

lst=[1,2,3,[10,20,30]] #列表的长度为4，这四个数据的类型是什么，前三个是int类型（不可变对象），第4个是列表，列表是可变序列

# 深拷贝 与浅拷贝 都指   可变序列， 不可变对象，不存在深与浅的问题
# 浅拷贝 是这样，使用copy中的copy函数（）
lst2=copy.copy(lst) # 浅拷贝
 # 浅拷贝 是外变，里不变
print(id(lst),id(lst[3])) # 小列表的内存地址没变
print(id(lst2),id(lst2[3])) # 小列表的内存地址变没变
lst[3].append(100)  # 向第一个列表中的 小列表填加元素
#lst和lst2中元素一样吗？

print(lst)
print(lst2)

print('-----------------深拷贝 是外变，里也变-------------------')
lst3=copy.deepcopy(lst)
print(id(lst),id(lst[3]))
print(id(lst3),id(lst3[3])) # 小列表的地址也发 生了变化

lst.append(200)

print(lst) # 只是向lst中添加了200
print(lst3) # 不会
