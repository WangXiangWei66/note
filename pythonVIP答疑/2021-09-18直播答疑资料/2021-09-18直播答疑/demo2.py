# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# *args  ：个数可变的位置参数
# **kwargs ：个数可变的关键字参数
def fun(*args,**kwargs):
    print(args)
    print(kwargs)

fun('hello','world',123) #args

fun(a='hello',b='world',c=123) # kwargs

fun('hello','world',123,a='hello',b='world',c=123)

# 路径的三种方式
file=open('d:/a.txt','r')

file2=open('d:\\a.txt','r')

file3=open(r'd:\a.txt','r') # 原字符，字符串中的所有转义字符都失效




