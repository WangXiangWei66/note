# coding:utf-8
# author:杨淑娟
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

    #重写父类的info方法
    def info(self):
        print(self.name,self.age,self.stu_no)


class Teacher(Person):
    def __init__(self,name,age,teacherofyear):
        super().__init__(name,age)
        self.teacherofyear=teacherofyear

    def info(self):
        print(self.name,self.age,self.teacherofyear)

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)

stu.info()
teacher.info()