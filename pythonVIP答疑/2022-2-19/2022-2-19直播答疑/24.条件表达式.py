# coding:utf-8
# author:杨淑娟
x=eval(input('请输入一个整数:')) # input()函数的结果是一个字符串类型，使用eval之后，就将字符串转成实际的数据类型
y=eval(input('请输入另一个整数:'))
print(type(x),type(y))

# 这两个整数进行比较大小的操作
#使用条件表达式
max=x if x>y else y
print('最大值为:',max)