# coding:utf-8
# author:杨淑娟
#普通的函数的定义方法
def fun():
    pass
# 如果函数体只有一句代码，可以使用lambda表达式（匿名函数）

# lambda的简单写法
def  fun2(x):
    return x+2
print(fun2(10)) # 输出结果是12

# 使用lambda表达式对fun2进行简化
f=lambda x:x+2    #  ：之前是参数，  ：之后是函数体
print(f(10))

print('---------------------------')
lst=[10,20,30,40] # 创建一个列表
#使用lambda表达式遍历列表中的元素
for i in range(len(lst)): # i的取值为0，1，2，3
    z=lambda x:x[i]   # x是参数，在这里代表的是列表 x[i]代表的是根据索引获取列表中的元素
    print(z(lst))


# 在进行列表排序时，也会使用到lambda
lst2=[
    {'name':'marry','age':20},
    {'name':'jack','age':18},
    {'name':'lucy','age':22}
]
# 按照年龄排序还是姓名排序呢？  x在这里代表的是字典，列表中的元素是字典 x['age']根据key获取value值
lst2.sort(key=lambda x:x['age']) # 据据年龄排序,升序
print(lst2)

