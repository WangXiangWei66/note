# coding:utf-8
# author:杨淑娟

lst=[1,2,3]
print(id(lst))
# 添加元素
lst.append(4)
print(id(lst))


x=10
print(id(x))
x+=2
print(id(x))  # 修改值之后，内存地址发生了改变，不可变对象