# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

num_in=int(input('请输入一个数:')) # 从键盘输入一个整数

def fib(num):   #函数的定义
    if num<=0:  #判断　
        raise  Exception('数字应该大于0!')#手动抛出异常
    if num==1 or num==2:  #判断
        return 1 #返加结果
    else:
        return fib(num-1)+fib(num-2) # 递归操作

# 从第三项开始，第三项=前两项的和
#斐波那契数列    1  1  2   3  5   8   13  21   34   55    89 ...
        #位置   1  2  3   4  5   6   7   8    9   10    11 ...


print(fib(num_in))  # 输入一个整数，输出结果为  num_in这个位置上的数字


fib_lst=[fib(i) for i in range(1,num_in+1)]  # 列表生成式 结果是 斐波那契数列的结果
fib_lst1=[fib(num_in) for i in range(1,num_in+1)]# 10个55 为什么是10个，因为num_in=10
print(fib_lst)
print(fib_lst1)
