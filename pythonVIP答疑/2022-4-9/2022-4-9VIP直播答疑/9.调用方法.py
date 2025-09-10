# coding:utf-8
# author:杨淑娟


#增值操作符
foobars=0 # 赋个初始值

foobars+=1 # 报错

class Student:
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def show(self):
        print(self.name,self.age)

    #类方法
    @classmethod
    def cm(cls):
        print('这个是类方法')


#调用实例方法的两种方式
# 建议使用这种   对象名.方法名（）的方式
s=Student('marry',20)  # 创建对象，自动调用__init__()方法
s.show() # 对象名.方法名()


# 类名调用
Student.show(s)  # 类名.实例方法名(对象）  方法的调用处，s是实参，方法的定义处17行,self是形参，self=s
