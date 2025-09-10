# coding:utf-8
# author:杨淑娟
import demo1
print(demo1.x) # demo1中x变量的值


#print(x)  # 输出的是本文件中的x的值

from demo1 import  x  #
print(x) # 输出的是helloworld

# 在想输出本模块中的x,将无法输出
print(x)
x='python is very good'
# 如果两个模块中有同名的变量，在导入时，只能使用import导入模块，使用使用"模块名.变量名"的方式调用
                            # 使用from ...import 的形式，变量的将会被覆盖
print(x)