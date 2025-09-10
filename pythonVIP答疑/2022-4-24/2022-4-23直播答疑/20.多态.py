# coding:utf-8
# author:杨淑娟
class Cat():
    def eat(self):
        print('猫吃鱼')

class Dog():
    def eat(self):
        print('狗吃骨头')

class Person():
    def eat(self):
        print('人吃五谷杂粮')

def show(obj):  # 传的是对象 ，什么类型的对象，不知道
    obj.eat()  # 调用对象的eat()方法，什么类型的对象不重要，重要的是具有eat方法

if __name__ == '__main__':
    c=Cat()  # 创建对象
    d=Dog()# 创建对象
    p=Person()   # 创建对象

    show(c) # 调用方法，
    show(d)
    show(p)