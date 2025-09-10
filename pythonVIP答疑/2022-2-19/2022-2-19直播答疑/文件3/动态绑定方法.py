# coding:utf-8
# Author: Wu Xiaofeng
# Data: 2022/2/17 23:12

import types  # 导入内置模块，不需要安装就可以使用
class Person:   # 定义了一个Python类，默认继承object类
    num=0       # 类的属性
    '''定义类'''
    def __init__(self,name,age):  # 类的初始化方法
        self.name=name
        self.age=age

    def eat(self):            # 类的实例方法
        print(self.name+' eat food')



p=Person('liubei',25)#实例化类的实例对象  （创建类的实例对象）

p.eat()              # 调用实例方法

#在外部定义一个函数show
def show():
    print('我是外部函数')

p.show=show #动态绑定方法   # Person类是没有show方法  ，=右侧的show指的是外部自定义的函数名称  ,加()是函数调用，不加()是赋值


p.show()   # 对象名.方法名（）


#肖老师课程中讲的，动态绑定方法
def run(self,speed):                 #在类的外部定义的函数
    print(f'{self.name}在移动，速度是{speed}km/h')


#动态绑定方法
p.run=types.MethodType(run,p)   # 使用的是内置模块types中MethodType里，进行绑定方法
p.run(100)   # 对象名.方法名（）
