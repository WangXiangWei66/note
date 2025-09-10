#教育机构 ：马士兵教育
#讲    师：杨淑娟
class Student(object):
    #类方法， 其中cls表示的是Student的类对象
    @classmethod
    def fun(cls):
        print('classmethon')

    @staticmethod
    def fun2():  #静态方法，没有任何默认参数
        print('staticmethon')

#所使用的方式相同
Student.fun()  #调用类方法
Student.fun2() #调用静态方法