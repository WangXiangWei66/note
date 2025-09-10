# coding:utf-8
# author:杨淑娟
class Person():  # 这是一个类   PersonH是类的名称, ()中什么都没写,默认继承object
    def __init__(self,name,age): # 小括号中的变量，称为局部变量，只在该 方法内起作用
        self.name=name  # 等号的左边是成员变量(实例属性)，等号的右边是局部变量
        self.age=age # 成员变量的使用范围是本类中，子类中
        self.__gender='女' # 私有的

    def __call__(self, firend):   # 这个__call__以是双 _ 开头和结尾的方法，是一个特殊的方法，
        print(self.name,self.age)
        print(f'{firend}是我的好朋友')

    def __str__(self):   # 有一个向上的箭头，还有一个蓝圈，带有字母o，这个o表示的是override
        return  self.name+str(self.age)

    def show(self):
        print('')
p=Person('张三',20)  # 创建Person的对象，对象名 是 p
p('李四')    # 对象变成函数调用
# 为什么对象可以变成函数调用呢？ 因为 Person类中有__call__方法，如果没有该 方法则不可以这样使用

print(p) # 在没有重写str方法前，输出的结果是内存地址 ,重写该方法后，则输出自定义的结果

print('----------------------------')
#print(p.__gender)  私有的是不允许在类的外类使用的，但是也不是不能使用
print(dir(p))
print(p._Person__gender) # 这样也可以访问到类的私有属性