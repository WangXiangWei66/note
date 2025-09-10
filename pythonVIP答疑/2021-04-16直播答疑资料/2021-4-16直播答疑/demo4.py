# 教育机构：马士兵教育
# 讲    师：杨淑娟

def fun():
    for i in range(5):
        return i
print(fun())#函数调用的结果是什么？　结果为０，循环第一次就结束函数了，根本没机会进行第二次循环
print('-----------------------------')
def fun2():
    for i in range(5):
        yield i

#print(fun2()) #<generator object fun2 at 0x00000225B8B3DAC0>　这是一个生成器对象,并没有获取i的值
# 迭代是一种操作， 迭代器是一个对明
a=fun2()  #a叫迭代器对象
print(a.__next__()) # 以下这种__next__()操作就称为迭代操作
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

'''
return 是用于结束函数
yield  用于保存函数在暂停，继续下一次的状态

'''
