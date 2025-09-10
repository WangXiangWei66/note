# coding:utf-8
# author:杨淑娟
lst=[10,20,30,43]
def fun(x):
    return lambda x:x%2>0
print(list(filter(fun(lst),lst)))