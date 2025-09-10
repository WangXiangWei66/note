# coding:utf-8
# author:杨淑娟
class FatherA():
    def __init__(self,name):
        self.name=name

    def father(self):
        print('父类A')

class FatherB():
    def __init__(self,name):
        self.name=name

    def father(self):
        print('父类B')

class Son(FatherB): # 直接修改父类  ,子类无需多加修加，程序就可以执行

    def __init__(self,name,age):
        super().__init__(name) #调用父类的初始化方法
        self.age=age

    def show(self):
        super().father() #调用父类的实例方法

son=Son('marry',20)
son.show()

