# coding:utf-8
# Author: Wu Xiaofeng
# Data: 2022/2/17 23:12

import types
class Person:
    num=0
    '''定义类'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+' eat food')
p=Person('liubei',25)#实例化类
p.eat()
#在外部定义一个函数show
def show():
    print('我是外部函数')
p.show=show #动态绑定方法
p.show()
#肖老师课程中讲的，动态绑定方法
def run(self,speed):
    print(f'{self.name}在移动，速度是{speed}km/h')
#动态绑定方法
p.run=types.MethodType(run,p)
p.run(100)
