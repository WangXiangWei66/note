#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# *args与 **kwargs是在函数定义时使用到
# *args :个数可变的位置参数
# **kwargs ：个数可变的关键字参数
# 如果同时出现在一个函数定义中，*args在前,**kwargs在后
def fun(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

# 函数的调用
fun(10,20,30,40,c=100,d=300,e=90)
    # 10,20是位置参数，分别赋值给a,b  ,30,40,个数可变的位置参数，赋值给args，结果为元组
    # c,d,e 是个数可参的关键字参数，赋值给kwargs



