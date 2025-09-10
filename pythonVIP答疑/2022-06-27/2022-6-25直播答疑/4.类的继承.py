# coding:utf-8
# author:杨淑娟
class A():
    def fun(self):
        pass
class B():
    pass

class C(A,B):
    def fun(self):
        print('子类重写了父类的的方法')