# coding:utf-8
# author:杨淑娟
class Father():
    def a(self):
        print('Father .a')

class Son(Father):   # 这叫继承
    def show(self):
        super().a() # 表示使用的是父类(Father)中的a
    # super()出现在子类中，，调用父类的属性或方法

# 缩进的地方
if True:
    pass
else:
    pass

for item in 'hello':
    pass


def show():
    pass

class A():
    pass


