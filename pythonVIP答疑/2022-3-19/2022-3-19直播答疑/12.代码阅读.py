# coding:utf-8
# author:杨淑娟
m=[1,2] #
n=m
n.append(3)
print(m)

# 拷贝
import copy   # 导入内置模块copy
n=copy.copy(m)  # 调用copy模块中的copy函数 ，进行都拷贝，拷贝完成之后,n是一个独立的地址空间
n.append(4)   # 向n添加4 ，m不会变
print(n)
print(m)

# 函数返回值
def info(name,gender):
    return  'name',name  # 'name':name  报错原因是语法错误
    return 'gender',gender   # 这句代码没有机会执行

print(info('张三','男'))


def func(a,b):   # a的值是10,b的值是100
    c=a**2+b   # c=10*10+100
    b=a
    return c    # 结果  200


a=10
b=100
c=func(a,b)+a
print(c)  # 结果是210