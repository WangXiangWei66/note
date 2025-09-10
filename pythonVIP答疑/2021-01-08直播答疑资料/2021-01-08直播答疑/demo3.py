# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 单父亲
class Person(): #()中什么都没写，默认继承的是object
    # 使用参数去给类的属性赋值
    def __init__(self,xingming,age): #name,age是__init__函数的参数，局部变量
        self.name=xingming  # self.name是Person类的属性
        self.age=age

    def show(self): #类中show方法
        print(self.name,self.age,end='\t')

class Student(Person): #Student继承了Person
    def __init__(self,name,age,score):
        #需要调用父类的初始化方法
        #super().__init__(name,age)
        Person.__init__(self,name,age) #注意事项，千万别忘了传第一个参数
        self.score=score
    def show(self):
        #super().show()
        Person.show(self)
        print(self.score)


class Sing():
    def __init__(self,song_name):
        self.song_name=song_name

    def singing(self):
        print('唱了一首名称为《',self.song_name,'》歌')


class Student2(Person,Sing):
    def __init__(self,name,age,song_name): #由于继承了两个父类，所以需要调用调用两个父类的初始化方法
        Person.__init__(self,name,age) #调用Person类的初始化方法 ，给name,age赋值
        Sing.__init__(self,song_name) #调用Sing类的初始化方法，给song_name赋值

    def show(self): #Student2中的show方法
        Person.show(self) # 调用父类的show方法
        Sing.singing(self) #调用Sing类中的singing方法

    # 听得懂，说明老师讲的好，做不出来，说明欠练

stu=Student2('张三',2,'石家庄加油')
stu.show()
# 在模块中使用def 定义的称为函数，在类中使用def 定义，称为方法
#
# p=Person('张三',20)
# print(p.name,p.age)
# #Python可以动态绑定类的属性
# p.gender='男'
# print(p.gender)





