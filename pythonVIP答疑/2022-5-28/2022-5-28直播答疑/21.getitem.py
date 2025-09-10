# coding:utf-8
# author:杨淑娟
class Person(): # 定义一个类 ,没有继承的时候()可写可不写，默认继承object类
    def __init__(self,lst): # 这是一个特殊的函数，这个函数在创建对象时自动调用 ,lst是一个位置参数
       self.lst=lst  # self.lst是对象的属性   lst是方法的参数（局部变量)

    def __getitem__(self, item): # 这也是一个特殊函数 item是方法的参数
        return self.lst[item]   # self.lst 这是列表  [item]列表取值


lst=['hello','world','python'] # 定义一个列表，三个元素

p=Person(lst)  # 创建Person类型的对象，并将lst传参赋值给self.lst

for item in p: # 遍历p对象，为什么可以直接遍历p对象呢？因为Person类具有__getitem()方法
    print(item) # 列表中的元素


class Person:
    def __init__(self,lst):
       self.lst=lst
       self.count=len(self.lst)

    def __iter__(self): # 如果类中没有__getitem__方法，具有iter 和next方法也可以进行遍历

        return self
    def __next__(self):

        yield self.lst[self.count-1]
        self.count -= 1

p=Person(['hello','world','python'])
print(tuple(p.__next__())[0])
print(tuple(p.__next__())[0])
print(tuple(p.__next__())[0])
