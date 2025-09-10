# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class person:
    def eat(self):
        print('人吃五谷杂粮')

#定义一个函数
def fun(animal): # animal就是参数，这个参数是对象类型
    animal.eat()

fun(Cat()) # 传的是Cat() 创建是Cat类的对象 ，调用当然是Cat类的中方法
fun(Dog())  #传的是Dog(),创建的是Dog类的对象，调用的当然是Dog类中的方法
fun(Animal())
fun(person())
