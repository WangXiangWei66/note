# coding:utf-8
# author:杨淑娟
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #这是父类中的实例方法，该 方法没有返回值，return ,使用的是print打印输出
    def info(self):
        #print(f'{self.name} is {self.age} years old')
        return f'{self.name} is {self.age} years old'

class Student(Person):
    def __init__(self,name,age,studentnumber):
        super().__init__(name,age)
        self.no=studentnumber

    def info(self):
        #这是调用处，调用处在处理返回值
        print(super().info())# 子类调用父类的实例方法   这句代码是否执行了?执行了，为什么没有输出，因为没有处理返回值
        return  f'{self.name}的学号是{self.no}'  # 子类有返回值


stu1=Student('张三',20,'10000')  # 创建学生对象

#调用info方法
print(stu1.info())  # 子类的返回值在这里打印