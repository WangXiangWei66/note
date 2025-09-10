# coding:utf-8
# author:杨淑娟
class Person:

    def __init__(self):
        self.name='张三'   # 带self ,可以在整个  Person类中的任意方法中使用
        age=20            # 不带self  ，因为age的使用范围仅限于__init__方法 ，出了这个方法就不能用了


    def show(self):
        print('姓名:',self.name)
        print('年龄:',age)  #NameError: name 'age' is not defined ， 不是在__init_中定义过了吗？为什么要这里不能使用

if __name__ == '__main__':
    p=Person()
    p.show()