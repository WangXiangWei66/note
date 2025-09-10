# coding:utf-8
# author:杨淑娟
# 定义处
def show(*args): # 定义处的参数为形参 ,加一颗星就是个数可变的位置形参
    print(args)



#调用处 ,参数的个数可变，
show(1)
show(1,2)
show(1,2,3)
show(1,2,3,4)

# 定义处 ，
def fun(**kwargs): #两颗星就是个数可变的关键字参数
    print(kwargs)

# 调用处
fun(a=10,b=20)   # a与b叫关键字 ,a和b可不可以换别的字母，可以
fun(x=100,y=200,z=300)  # 关键字的名称自己起 ，调用处的关键字，叫什么都行
