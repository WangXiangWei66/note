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

one = lei(3, 4, 5)
one.show1()
one.show2()
one.show3()
list = ['show1()', 'show3()'] # 列表中的数据是字符串类型
for i in list:
    print(one.i)  # one.'show1()'
    #one.(eval(i))

