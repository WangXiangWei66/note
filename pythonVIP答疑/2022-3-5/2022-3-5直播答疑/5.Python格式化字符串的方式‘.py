# coding:utf-8
# author:杨淑娟
#（1）使用%的形式
name='Marry'
age=20
print('姓名:%s,年龄:%d' % (name,age))  #  (name,age)元组类型 %s 代表的是字符串 %d代表的是整数

#（2）使用字符串的format方法
print('姓名:{0},年龄:{1}'.format(name,age))

#（3）使用f-string的形式
print(f'姓名:{name},年龄:{age}')

print('身高为%.2f'%183.4) # 保留两位小数
# Python中的缩进相当于其它语言中的{}



print('---------------------------------------')

class Person():
    #成员方法，该 方法是由对象名打点调用
    def fun(self):
        print('我是fun方法',self)

    @classmethod   # 类方法的修饰  ， 类方法是使用类名打点调用
    def methon(cls):
        print('我是类方法methon',cls)

p=Person() # 创建Person类型的对象
p.fun()


#类方法的调用
Person.methon()
if True:
    pass

while True:
    pass

def fun():
    pass

class Student():
    pass
