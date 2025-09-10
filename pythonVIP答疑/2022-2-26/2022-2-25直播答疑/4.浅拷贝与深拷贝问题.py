# coding:utf-8
# author:杨淑娟
import  copy # 导入内置模块copy
m=[1,2]
n=copy.deepcopy(m) # 用到的是一个深拷贝
print('m的id',id(m))
print('n的id',id(n))
n.append(3)
print(m)
print(n)
#以下两句代码的内存地址完全相同，因为int是不可变对象，
print(id(m[0]))
print(id(n[0]))

# 可以不可以使用浅拷贝 呢？
z=copy.copy(m)
z.append(3)
print(m) # m是1,2
print(z) # z是1,2,3

# 要想让n进行append的时候m的值不发生变化，可以使用深拷贝 和浅拷贝

# 对于不可变对象， 深拷贝 与浅拷贝 结果相同

# 深拷贝 与浅拷贝 的不同点
lst=[10,20,[30,40,50],(60,89)] # 列表中4个元素，   两个整数，一个列表，一个元组，其中 列表是可变序列
                                              # 整数和元组是不可变对象
print('-----------lst与lst2的内存地址不同----------------')
# 开始进行浅拷贝
lst2=copy.copy(lst)
print(id(lst))
print(id(lst2))
#
print('------------lst与lst2中元组的内存地址相同--------------')
print(id(lst[2]))
print(id(lst2[2]))

print('--------------深拷贝 ，列表的地址不同，列表中可变对象的地址也不同-----------------------')

lst3=copy.deepcopy(lst) # 深拷贝
print(id(lst))
print(id(lst3))

print('--------列表中元素（可变对象）地址也不同-----------')
print(id(lst[2]))
print(id(lst3[2]))
