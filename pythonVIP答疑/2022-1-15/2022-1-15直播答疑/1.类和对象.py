# coding:utf-8
# author:杨淑娟
class Person:
    #实例方法
    def fun(self):
        pass

    #类方法
    @classmethod
    def show(cls):
        print(id(cls))
        pass

    #静态方法
    @staticmethod
    def method():
        pass
    pass

p=Person() #p就是Person这个类的实例对象，相当于 Word文档中的那个 “可以吃的月饼”

#类方法使用类名去调用
Person.show()
print(id(Person))  # Person这个类id与类方法中cls的id相同，所以说cls指的是 Person这个类


