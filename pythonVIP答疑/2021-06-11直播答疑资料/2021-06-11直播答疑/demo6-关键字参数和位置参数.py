#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
def fun(a,b,c ): #函数的定义处
    print(a,b,c)
# 函数的调用处
fun(10,20,30) # 位置传参
fun(c=30,a=10,b=20) # 关键字传参
print('------------------------------')
def fun(a,b,**kwargs):# 个数可变的关键字参数
    print(a,b)
    print(kwargs)
fun(10,20,c=100)
fun(a=10,b=20,c=100) # 写法相同含义不同

def fun(*args,**kwargs): # 个数可变的位置参数， 个数可变的关键字参数
    print(args)
    print(kwargs)
print('----------------------------------')
fun(10,20,c=30)
fun(a=10,b=20,c=30)





