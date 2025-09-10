#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)


class Student(Person):
    def __init__(self,name,age,student_num):
        Person.__init__(self,name,age)
        self.student_num=student_num

class Teacher(Person):
    def __init__(self,name,age,teacher_num):
        Person.__init__(self,name,age)
        self.teacher_num=teacher_num

'''
继承多个父类，在调用父类初始化方法时，只能使用类名的形式,否则区分不开父类
'''
class Stu_Teach(Student,Teacher):
    def __init__(self,name,age,student_num,teacher_num,gender):
        #super().__init__(name,age,student_num)
        Student.__init__(self,name,age,student_num)
        Teacher.__init__(self,name,age,teacher_num)
       # super().__init__(name,age,teacher_num)
        self.gender=gender

    def info(self):
        print(self.name,self.age,self.student_num,self.teacher_num,self.gender)
stu_teach=Stu_Teach('xx',21,'msb1001','js007','男')
stu_teach.info()