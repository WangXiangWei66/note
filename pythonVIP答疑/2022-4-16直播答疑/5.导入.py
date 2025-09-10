# coding:utf-8
# author:杨淑娟

# 有两种导入方法 1）使用import 导入
import Calc                            # 导入模块中的所有
# 使用Calc中的函数，模块名称打点调用
print(Calc.add(10,20)) # 结果就是30
print(Calc.sub(20,10))


# 2)第二种导入方式 from xxx import yyyy   # 导入模块中的一部分
from Calc import add # 导入的是add函数  只能使用add函数，如果要使用sub函数，则还需要导入
# 直接函数名称即可调用
print(add(20,30))

#
from Calc import *
