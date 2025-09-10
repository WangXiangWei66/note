# coding:utf-8
# author:杨淑娟
class Animal:
    def talk(self):
        pass
class Dog(Animal):
    def talk(self):
        print('小狗汪汪叫')

class Cat(Animal):
    def talk(self):
        print('小猫喵喵叫')

class Frog():     #  这个不是Animal的子类 ，默认继承的是obejct类
    def talk(self):
        print('青蛙呱呱叫')

def show(obj):   # 谁去做方法的参数？是Animal吗？不是, 是object ，object可以是任意类的对象，只要具有talk()方法
    obj.talk()

if __name__ == '__main__':
    show(Cat())  # 创建Cat类
    show(Dog()) # 创建Dog类

    show(Frog()) # 创建Frog类   Frog与Aniaml没关系的