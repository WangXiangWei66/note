# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

def fun1(*a): # 自定义的函数
    print(a)


def fun2(**b): #自定义的函数
    print(b)


tpe = (11, 22, 33, 44, 55)
lst = [1, 2, 3, 4, 5, 6]
dic = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
set1 = {31, 32, 33, 34, 35}

print('*tpe', end=' ')
fun1(*tpe)  # 元组
print('*lst', end=' ')
fun1(*lst) #列表

print('*set1', end=' ')
fun1(*set1) # 集合
print('*dic', end=' ')
fun1(*dic) #字典

print('**dic', end=' ')
fun2(**dic)#字典
print('**tpe', end=' ')
# fun2(**tpe)
# print('**lst', end=' ')
# fun2(**lst)
# print('**set1', end=' ')
# fun2(**set1)
