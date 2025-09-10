# coding:utf-8
# author:杨淑娟
for n in range(2,3):   # 外层循环可以执行的次数  2<=n<3
    for x in range(2,2):  # 内层循环    2<=x <2  有这样的数吗？ 没有，所以内层循环一次都没执行
        if n%x==0:
            print(n,'等于',x,'*',n//x)
            break
    else:                 # 直接执行的是else部分
        print(n,'是质数')  # 输出了2是质数




print('--------------------')
s='an apple a day'

def split(s):
    return s.split('a')
print(s.split())  # 为什么没有按照a分开  ，调用是 字符串对象的split方法
print(split(s)) # 才是调用自己定义的函数并传参