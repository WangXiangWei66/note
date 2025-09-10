# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
#  
def fun(param):
    if param==1 or param==2:  # 判断的是递归的结束条件
        return 1   # 第一项或第二项上的数字都是1

    else:  # 函数的调用（自己调用自己)
        return fun(param-1)+fun(param-2)

print(fun(8))

print('N的阶乘') # 5!=5*4*3*2*1


def fun(param): # param代表的是要计算阶乘的数
    if param==1:  # 判断的是递归的结束条件
        return 1     # 1的阶乘就是1
    else:  # 函数的调用（自己调用自己)
        return param*fun(param-1)   #   N*fun(N-1) 举例  5！=5*4！

print(fun(5))
