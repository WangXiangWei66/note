# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

# 这是一个装饰器函数
def fun(func): #func是一个函数
    print('装饰上花朵，装饰上蜡烛')
    return func # 返回函数

#对蛋糕进行装饰
@fun          # @  这是一个装饰函数，修饰后面那个函数的行为
def cake():
    print('我是一块蛋糕')

# 调用方式
cake()