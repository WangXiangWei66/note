#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
class Person:  #如果一个类没有继承任何类，默认继承ｏｂｊｅｃｔ类
    # 初始化方法，作用：是给类的属性赋值
    def __init__(self,xm,nl):  #__init__ 方法是Person的父类 object中的方法
        self.name=xm # 类的属性叫self.name 赋的值为xm,这个xm值会在创建对象时传入
        self.__age=nl # 类的属性self.age

    def get_age(self):
        return self.__age
    def  __show(self):
        print(self.name,'-----------',self.__age)
# 创建类的对象
p=Person('张三',30) # 相当于xm='张三' ,nl=30 赋值操作
print(p.name)
#print(p.__age) # 运行时报错AttributeError: 'Person' object has no attribute '__age'

print(p.get_age())

# 只能通过定义方法去访问__age的值吗？
print(dir(p))

# 不能直接p.__age访问的， 但是可以p._Person__age进行访问
print(p._Person__age)
print('---------------------------')

#p.__show()  直接调用私有方法报错
#解决方案
p._Person__show()  # 尽量不采用这种方式调用“私有”方法

# Python中的封装，主要靠程序员的自觉
