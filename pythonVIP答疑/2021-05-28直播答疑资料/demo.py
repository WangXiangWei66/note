#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
from operator import attrgetter
lst=[str(i) for i in range(10)] #列表生成式
print(lst)
lst2=[ord(i) for i in lst] # 列表生成式 ord(i)将字符转成应的unicode码

print(lst2)

lst3=['a','b','0','A']
lst3.sort()
print(lst3)

# 自定义类如何排序
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person('marry',20)
p2=Person('lili',19)
p3=Person('jack',22)
p4=Person('rose',24)

# 列表中存储了4个Person类型的对象
lst4=[p1,p2,p3,p4]
lst4.sort(key=attrgetter('age')) #根据age属性进行排序
print(lst4)
for item in lst4:
    print(item.name,item.age)

# 同学的代码
lst5=[[1,34,34],[5,6,7,7,8,5],'hello','heloworld']

# 函数的功能，求对象的长度
def f(x):
    return len(x)
#lst5.sort(key=f) # 按照函数f进行排序
lst5.sort(key=lambda x:len(x)) # 使用匿名函数
print(lst5)
