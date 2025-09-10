# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 迭代器与和生成器
# 一个迭代器对象，底层实一邮__iter__()和__next__()的方法
import sys
# A 类去实现以上两个方法，A类的实例对象，可以创建迭代器对象
# class A:
#     def __iter__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         if self.a<=10:
#             x=self.a    # 存储当前值
#             self.a+=1    # 其值自增1
#             return x    #返回当前值
#         else:
#             raise  StopIteration #底线，超为10就报错
# a=A() # 创建A类的实例对象
# # 通过a类的实例对象，创建迭代器对象
# t=iter(a) # t就是迭代器对象
# # 调用next方法进行迭代取值
# print(next(t)) # 1
# print(next(t)) # 2
# print(next(t)) # 3
# print(next(t)) # 4
# print(next(t)) # 5
# print(next(t)) # 6
# print(next(t)) # 7
# print(next(t)) # 8
#
# print(next(t)) # 9
# print(next(t)) # 10
#
# #print(next(t)) # 11?
#
# print('-----------------------------')
# # 列表也可以创建迭代器对象
# lst=[10,20,30,40]
# t2=iter(lst) # t2就是迭代器对象
# print(next(t2))
# print(next(t2))
# print(next(t2))
# print(next(t2))
#
# # 普通的类可以创建迭代器对象
# class B:
#     pass
# b=B()
# #t3=iter(b) # object is not iterable因为B没有实现__iter__()和__next__()两个方法
# #print(next(t3))
#
# # 请问，str,元组，字典，集合，列表，int可以创建迭代器对象吗？
# #　前5个可以，第6个int不可以
# # 前5个都可以使用for..in 循环
# '''
#   迭代器对象：  类实现了两个方法__iter__, __next__
#   生成器对象 :  方法中使用了yield关键字
#              生成器本身也是一个迭代器对象
# '''
# print('--------------------生成器对象 （方法使用了yield关键字）----------------')

# yield 结束方法，并保留方法的运行结果，下次调用时，从yield这后的代码执行

# 斐波那契数列
#　实现方式１.　循环 ，2.递归算法  3.yield实现
'''        a     b
      a    b   (0+1)
数列  0    1     1     2     3      5     8     13    21    34.....
位置  1    2     3     4     5      6     7     8     9     10
'''

def fibo(n):  # n表示的是第几位上的数字
    a=0 # 代表第一个位置上的数
    b=1  # 代表第二个位置上的数
    counter=0  #统计执行次数，
    while True:
        if counter>n:
            return  # 结束方法

        yield  a   # 结束方法，记录当前a的值，下次调用方法是时，使用下一句代码开始执行
        # a=b  # 将b的值赋值a， 将a+b的值赋给b
        # b=a+b    a=b,  b=a+b这两句代码是错误的，交换两个变量的值，应该使用第三变量
        a,b=b,a+b  #如果不使用第三变量， 使用Python的解包赋值
        counter+=1

#调用
f=fibo(10) #ｆ是一个迭代器，这个迭代器由生成器生成的
while True:
    try:
       print(next(f))
    except StopIteration:
        sys.exit()





