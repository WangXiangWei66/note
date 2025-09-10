#教育机构 ：马士兵教育
#讲    师：杨淑娟
'''Python中一切皆对象 '''
class Person(object):
    def __init__(self,name,age):  #初始化函数，用于给类的对象进行属性赋值
        print(f'__init__方法被调用执行了,self的id值为{id(self)}')
        self.name=name #将局部变量name的值赋值给成员变量self.name
        self.age=age


    def __new__(cls, *args, **kwargs): #用于创建对象的
        print(f'__new__方法被调用执行了，cls的值id值为{id(cls)}')
        obj=super().__new__(cls) #获取创建的Person类型的（实例）对象
        print(f'创建的对象(obj)的id值为:{id(obj)}')
        return  obj


print(f'object类的这个类对象的id值为:{id(object)}')
print(f'Person类的这个类对象的id值为:{id(Person)}')
per=Person('Jack',20) #创建Person类的实例对象
print(f'per1这个Person为型的实例对象的id值为{id(per)}')

per.gender='男'  #动态绑定属性
print(per.gender)

# del per
# print(f'per1这个Person为型的实例对象的id值为{id(per)}')
# print(id(Person)) #获取类对象的id  2818371818352
# print(type(Person)) #获取类对象的数据类型  <class 'type'>
# print(Person)  #获取类对象的value值 <class '__main__.Person'>



