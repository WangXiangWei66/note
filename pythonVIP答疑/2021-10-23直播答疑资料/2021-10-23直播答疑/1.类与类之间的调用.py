# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

class A:
    def __init__(self,data):
        self.data=data

class B:
    def __init__(self,obj):
        self.obj=obj

a=A(10)
print(a.data)

#创建B类的对象
b=B(a)
b.obj.data=1000   #b.obj.data  是不是A类是的self.data
print(a.data)