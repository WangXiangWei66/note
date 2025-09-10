# coding:utf-8
# author:杨淑娟
a=100
def fun():
    global  a
    print(a) # 全局变量
    # 在函数中试图修改全局变量的值
    a=50

#调用函数
fun()