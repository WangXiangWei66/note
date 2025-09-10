#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

# 自定义类如何排序
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person('marry',20)

# 定义函数
def fun(obj): # 函数定义的参数为形参
    #obj=Person('marry',20)
    obj.name='Jack'

# 调用函数进行参数传递
fun(p1) #  函数调用处的参数为实参
print(p1.name)


