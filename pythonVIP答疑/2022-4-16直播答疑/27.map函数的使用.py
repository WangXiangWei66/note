# coding:utf-8
# author:杨淑娟
lst=range(1,11) # 产生个1到10之间的整数序列

def fun(x):   # 定义一个函数
   return x/2  # 函数的功能是 对x进行除以2的操作

# map函数的作用，是对lst中的每一个元素执行fun函数
lst1= map(fun,lst) # map函数的用法， map(第一个函数是函数名,第二个参数是一个可迭代序列)
print(list(lst1))
