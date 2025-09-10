# 教育机构：马士兵教育
# 讲    师：杨淑娟
class Person():
    def __init__(self,name): #name 是局变量，
        self.xm=name  # 左侧的self.xm 才是类的属性
        self.nl=20  #左侧的self.nl才是类的属性


class Student(Person):
    def __init__(self,name,stuno): #self相当于Java语言中的this
        super().__init__(name)  # self只作为函数定义时参数，函数调用时无需传参
        self.xh=stuno


stu=Student('marry','msb1001')
print(stu.xm)  # 对象名.属性名
print(stu.nl)

