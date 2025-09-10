# coding:utf-8
# author:杨淑娟
# 装饰器

import time
# 这是装饰器（闭包的应用场景）

def decorator(func):                   # 函数产生了嵌套 ，最外层的叫外层函数
    def wrapper(*args, **kwargs):    # 内层函数
        # 执行函数内部逻辑 打印时间
        print(time.time(), args, kwargs)  # 内层函数的函数体
        # 执行调用函数中逻辑 打印不同参数
        func(*args, **kwargs) #  被装饰的函数的调用
    return wrapper  # decorator的返回值是一个函数


# 上面是不是一个函数？是函数就可以调用

# def func():
#     print('fffffffffff')
#
# print(decorator(func)) # 正常的函数调用



# 一个参数  decorator 是上面那个函数的函数名称
@decorator               # 在这里，装饰 器，装饰是函数  function这个函数
def function(param):
    print('function : this is decorator ' + param)


# 两个参数
@decorator    # 装饰器，装饰的是function1这个函数
def function1(param1, param2):
    print('function1 : this is decorator ' + param1)
    print('function1 : this is decorator ' + param2)


# 三个参数（可变参数）
@decorator         # 装饰器，装饰的是function2这个函数
def function2(param1, param2, **kwargs):
    print('function2 : this is decorator ' + param1)
    print('function2 : this is decorator ' + param2)
    print(kwargs)


# -------------------被装饰的函数的调用---------------------------------
function('param')   # 字符串类型
function1('param1' , 'param2')   # 这是两个字符串，    为什么参数可以是一个，两个，多个？
function2('param1' , 'param2', x=1,y=2,z=3)
                                          # 因为装饰器中使用的是个数可变的位置参数，和个数可变的关键字参数