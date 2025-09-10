# 教育机构：马士兵教育
# 讲    师：杨淑娟
import sys
class A:
    pass

a=A()  # 创建了一个A类的实例对象，这个A类的实例对象就有了一个引用
print(id(a)) # A 类实例对象的地址为2566631134880 ，现在有一个引用叫做a
# 输出结果为2 ，  a=A() 一个引用数计数，调用sys.getrefcount(a)时，引用计数加1
print(sys.getrefcount(a)) # 可以查看对象的引用计数

# 方法调用 结束后，引用计数减1
# 对象的赋值也可以增加引用计数
b=a  # 实例对象的赋值，实际底层复制的是内存地址 ，引用计数+1
print(sys.getrefcount(a))#调用时加1，调用结束减1
#
#a对象存储到容器中（列表，字典，集合，元组）
lst=[a,a] # 引用两次，所以引用次数加2
print(sys.getrefcount(a))# a作为参数传入，引用计数也是要加1

# A类的实例好象会不会被Python的垃圾机制回收呢？
# 当引用计数为0时，Python的垃圾回收机制就会进行回收
print('------------------------------')
#什么情况下引用计数会减１呢？
#del lst[0]   # w从列表中将索引为0的元素删除
del lst # 删除列表
print(sys.getrefcount(a)) # 3

del b
print(sys.getrefcount(a)) #2

# del a   #A的实例对象上的引用，为0
# print(sys.getrefcount(a)) a#  name 'a' is not defined 程序报错


