# 教育机构：马士兵教育
# 讲    师：杨淑娟
class Person(object):
   city='北京'  # 类属性
   def __init__(self,name,age): #()中的name和age是方法的参数，等同时局部变量
        self.xingming=name     # name和age是程序员自定义的，想写多少个就写多少个
        self.age=age            # self是默认的，必须要写的，不写会报错的
                                #self.xingming 是类的实例属性  ,name是方法的参数
                                # self.age是类的实例属性，age是方法的参数
                               # 类的实例属性的名称和参数的名称可相同也可不同

   #　自定义对象，通常要重写str方法，目的是要显示对象的属性等内容
   def __str__(self):
        return  self.xingming+'\t'+str(self.age)

# Python中一切皆对象
# print(Person) #程序不报错，说明Person是一个对象，Person是一个类对象
# print(id(Person))  #2446353756368  Person这个类对象的在内存中的内存地方
#
# print(dir(Person))

# 创建Person类的实例对象
p1=Person('marry',20)   #创建了两个Person为的实例对象
p2=Person('lili',22)
p2.gender='女'

print(p2.xingming,p2.age,p2.gender) # 正常执行，不报错
#print(p1.xingming,p1.age,p1.gender) # AttributeError: 'Person' object has no attribute 'gender'

# 类属性的使用方式
print(Person.city) #输出结果是北京
print(p1.city)   # 结果都是北京
print(p2.city) # 结果都是北京
print('-------------------------------------------')
p1.city='上海'

print(Person.city)  # 北京
print(p1.city) #上海   ?  为p1动态绑定了一个实例属性叫 city
print(p2.city) # 北京

print('-------------object的特殊属性----------------------')
print(p1.__dict__)  # __dict__是object中一个特殊属性
print(p2.__dict__) #__dict__的作用，获取类对象或实例对象所绑定的属性和方法的字典

del p1.city  #  将p1对象动态绑定的实例属性删除了
print(p1.city) # 显示的依然是类属性
print(p1.__dict__)

del Person.city   # 进行了删除
print('--------------------------------')
#print(Person.city)  # 获取，报错

print('---------------------------------')
p2.city='天津'  # 重新为p2绑定city属性
print(p2.xingming,p2.age,p2.city)

print('-----------------------------------------------')
print(p1) #0x00000297803EA1F0
print(p2) #0x00000297803EA250




