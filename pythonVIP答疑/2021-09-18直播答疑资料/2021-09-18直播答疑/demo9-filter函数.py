# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
def fun(num):   # 就是一个普通的函数，可以被手动调用N多次
    return num%2==0   #这是偶数， 这个函数的返回结果为bool类型

lst=[1,2,3,4,5,6,7,8,9,10] # 这是一个列表

for item in filter(fun,lst):  # 得到的是一个偶数
    print(item,end='\t')


print('--------------------------')
for item in filter(lambda x:x%2==0,lst): # lambda是匿名函数，只能在这使用
    print(item,end='\t')