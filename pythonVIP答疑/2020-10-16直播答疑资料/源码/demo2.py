#教育机构 ：马士兵教育
#讲    师：杨淑娟
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stuno):
        #super().__init__(name,age) #调用父类Person的初始化函数
        Person.__init__(self,name,age)
        self.stuno=stuno

    def show(self): #方法重写
        #super().show()
        Person.show(self)
        print(self.stuno)

#创建对象并调用对象的实例方法show()
stu=Student('Jack',20,'10001')
stu.show()

class Sing(object):
    def __init__(self,song_name):
        self.song_name=song_name

    def singing(self):
        print('唱了一首<<',self.song_name,'>>的歌曲')

class Student2(Person,Sing):
    def __init__(self,name,age,stuno,song_name):
        Person.__init__(self,name,age) #Person类的
        Sing.__init__(self,song_name)
        self.stuno=stuno

    def show(self):
        Person.show(self)  #父类Person的show方法
        Sing.singing(self)
        print(self.stuno)

stu2=Student2('Tom',20,'1001','东方红')
stu2.show()