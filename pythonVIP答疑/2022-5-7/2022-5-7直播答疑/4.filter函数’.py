# coding:utf-8
# author:杨淑娟
#filter是一个内置的函数，
lst=[1,2,3,4,5,6,7,8,8,9,10] # 这是一个列表

def show(x):
    if x%2>0:
       return  x

reu=filter(show,lst) # 对lst中的每个元素，都会执行一次show方法
print(list(reu))
# for item in reu:
#     print(item)  # 取出了所有的奇数

#
#lambda 函数的使用
           # x是参数,  x%2是表达式（函数体） ，最后返回余数
z=lambda x:x%2 # x是一个参数 ,z就是函数名 在调时使用z()  ,计算x与2的余数

print(z(10)) # 还有一个参数x要传值   ，输出余的值
