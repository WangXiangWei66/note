# coding:utf-8
# author:杨淑娟
class lei(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def show1(self):
        print(self.a + self.b + self.c)
    def show2(self):
        print(self.a - self.b - self.c)
    def show3(self):
        print(self.a * self.b * self.c)

    def fun(self): # 类中定义的方法
        lst=[]
        lst.append(self.show1())  # 将调用的方法添加到列表中
        lst.append(self.show2())

        return lst
one = lei(3, 4, 5)
# one.show1()
# one.show2()
# one.show3()
list = one.fun()   # 对象名.方法名()，该 方法的返回值是一个列表
for item in list: # 遍历列表
    item   # 就是执行列表中的方法
