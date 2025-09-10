# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

class Student:
    # 定义实例属性
    def __init__(self,stuno,stuname,stuage): #stuno,stuname,stuage称为方法的参数
        self.no=stuno  # self.no为实例属性
        self.name=stuname #self.name为实例属性
        self.age=stuage# self.age为实例属性

# 实例属性的值是在创建对象时传入
stu=Student(1001,'张三',20)  #传入实例属性的值

#第二种，创建实例属性的方式，动态绑定
stu.gender='男'
print(stu.no,stu.name,stu.age,stu.gender)
