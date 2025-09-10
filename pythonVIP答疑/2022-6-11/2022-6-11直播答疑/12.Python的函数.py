# coding:utf-8
# author:杨淑娟
#（1）map函数，map函数用于将指定序列中的所有元素作为参数调用指定函数，并将结果构成一个新的序列返

def show(x):
    return x*2

lst=[1,2,3,4]
 # 将lst列表中的每一个元素都传到show方法中执行一次
result=map(show,lst) # 使用Python内置的map函数，map函数的第一个参数是一个函数名称（不带括号）
print(list(result))

#(2)filter函数，filter函数可以对指定的序列执行过滤操作。

def is_even(x):
    return x%2==0   # 与2的余数为0的就是一个偶数

result=filter(is_even,lst)  # 将lst中的每个元素都执行一次is_even，然后将偶数返回 ，偶数就是一个过滤的结果

print(list(result))

# (3)reduce函数，reduce函数用于将指定序列中的所有元素作为参数按一定规则调用指定的函数

from functools import reduce

def myadd(x,y):   # 相加操作 1+2+3+4
    return x+y

sum=reduce(myadd,lst)
print(sum)

# (4)zip函数,zip函数是以一系列的列表作为参数，将所有列表中对应的元素打包成一个个元组，然后返回这些元组组成的列表
lst2=['a','b','c','d']
result=zip(lst,lst2)
print(list(result))