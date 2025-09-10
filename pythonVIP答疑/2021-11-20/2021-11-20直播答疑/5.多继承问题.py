# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

class A:
    def fun(self):
        print('A类中的fun方法')

class B:
    def fun(self):
        print('B类中的fun方法')

class Child(A,B): # 多继承，手动调用父类的__init__方法了吗？
    def methon(self):
       A .fun(self) #使用父类的类名调用方法，很明确
    def fun(self):
        print('子类的fun方法')
c=Child()
c.methon()
c.fun()
