# coding:utf-8
# author:杨淑娟
import time

'''函数的名称为log, 函数体从7到10行'''
def log(fun):  # 函数的定义 fun 是函数的参数（fun的类型是一个函数类型）
    def a():   # 函数的嵌套（在一个函数里定义另外一个函数，就叫函数嵌套）
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),'正在执行函数',fun.__name__)
        return fun()  # 函数的返回值  （是调用fun()函数， fun函数是log函数的参数
    return a    # 函数的返回值，返回一个函数对象


# 函数要想执行，需要调用
# 想要调用log函数， 需要传一个参数，这个参数是一个函数对象
def   aa():
    print('helloworld')

# aa是一个函数，它将作为一个参数，被传入到log中
result=log(aa) # 函数的调用, 并处理返回值  ，这个返回值是一个函数，调用才能执行
result()
'''以上这种调用方式，很麻烦，有没有简便的方法呢？有'''

print('------------------------------------')

@log         # 这就是装饰器  （给函数做装饰的）
def bb():
    print('三餐四季，人间烟火....')

bb() # 直接调用bb

print('--------------还有另外的函数，也想输出日志信息,加@log----------------------')
@log
def show():
    print('春花秋月何时了')
    print('往事知多少')

show()