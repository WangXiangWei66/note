# coding:utf-8
# author:杨淑娟
class A:
    def show(self):
        print('a')

class B:
    def show(self):
        print('b')

# A类与B类之间不存在继承关系，只是两个普通的单独类，但具有同名的方法show

def fun(obj):  # 这个obj可能是A 类的对象，也可能是B类的对象
    obj.show() # 只知道这个obj对象有一个show方法

if __name__ == '__main__':
    a=A() # 创建A类的对象
    b=B()   # 创建B类的对象
    #调用fun函数
    fun(a)
    fun(b)


