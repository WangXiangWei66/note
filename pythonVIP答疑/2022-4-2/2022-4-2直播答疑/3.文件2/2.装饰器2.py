# coding:utf-8
# author:杨淑娟
def decorator(count):  # 有返回值没？
    a = 1
    b = 1
    count()   #  函数调用要加括号少
    def sum():
        c = 1
        #return a + c  # a - 自由变量   返回值  ，整数
        print(a+c)
    return sum   # 返回值是一个函数

@decorator
def count():  # 核心内容
    print("hello world....")

#print(count()) # 因为要输出sum()函数的返回值
print('----------------------')
count()  # 没有处理sum()函数的返回值