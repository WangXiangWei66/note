# Python自学
# 姓名: Liu JP
# 文件名: 继承及其实现方式.py
# 软件: PyCharm
# 开发日期：2022/7/29 11:33
print('-------------继承及其实现方式------------')
class Person(object): #Person继承了object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):
    def __int__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)

stu.info()
teacher.info()
