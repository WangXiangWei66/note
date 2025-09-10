# coding:utf-8
# author:杨淑娟
class Person(object):


    def __new__(cls, *args, **kwargs):
        print(f'__new__被调用执行了,cls的id值为{id(cls)}')
        obj=super().__new__(cls)           # 这个obj就是一变量，可以命名为a,也可以命名为b,为什么要命名为obj，因为obj是object（对象）的简称
        print(f'创建的对象id为{id(obj)}')
        return obj

    def __init__(self, name, age):
            print(f'__init__被调用了self的id值为{id(self)}')
            self.name = name
            self.age = age


if __name__ == '__main__':
    print(f'object这个类对象的id为{id(object)}')
    print(f'Person这个类对象的id为{id(Person)}')
    p=Person('marry',20)
    print(f'Person对象的id值为{id(p)}')