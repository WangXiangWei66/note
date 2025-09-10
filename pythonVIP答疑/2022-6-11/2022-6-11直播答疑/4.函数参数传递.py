# coding:utf-8
# author:杨淑娟
def show(a,b):
    sum=a+b
    return sum

# 函数的调用
x=10
y=20
result=show(x,y)  # 这个函数是有返回值
print(result)

print('--------------常见的异常类型-----------------------')
# （1）NameError
#print(hello)  # 这个hello没有加引号， 说明它不是字符串，它是一个变量名，但是这个变量又没有被声明

#（2）ZeroDivisionError
try:
    print(1/0) # ZeroDivisionError ,
except ZeroDivisionError:
    print('除数不能为0')

# （3）IndexError
lst=[1,2,3,4]  # 四个元素的索引为正向索引0，1，2，3 ， 逆向索引  -4,-3,-2,-1
print(lst[3],lst[-1])
#print(lst[5]) # IndexError

# (4)KeyError ,一般会在字典取值时出现问题
d={'a':1,'b':2,'c':3}
# 字典取值的方式有几种？
print(d['a']) # 正常
#print(d['d']) # KeyError
# 为了防止这种问题的产生，通常会使用get方法
print(d.get('d')) # None ,在使用字典取值时，建议使用字典对象的get()方法
print(d.get('d','这个键不存在'))

# (5)FileNotFoundError
#f=open('a.txt','r') # FileNotFoundError

# (6)AttributeError
print('hello'.kkkk) # AttributeError，这个kkkk是什么啊？字符串对象知道吗？不知道




