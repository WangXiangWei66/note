# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
# for i in range(5):
#     print(i)
# 姓名='杨淑娟'  # 姓名  为中文，所以不建议使用中文为变量，函数，模块，类，进行命名
# print(姓名)


class Student:
    stuno = 1001   # 类的属性
    _stuno = 100001 # 不能直接访问的类的属性

    def __init__(self, name, age):   # 以__开头并且以__结尾，   专用标识
        self.__name = name   #类对象的私有属性
        self.age = age


stu = Student('zhangsan', 20) # 会自动调用__init__()函数进行初始化
print(Student.stuno)  # 调用类的属性
#print(Student._stuno) # Access  to a protected member      警告

print(stu.age)   # 使用对象名调用Student类对象的属性
# print(stu.__name) # AttributeError: 'Student' object has no attribute '__name'
# print(dir(stu))
print(stu._Student__name)  # Access to a protected member 访问受保护成员










