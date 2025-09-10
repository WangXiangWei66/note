# coding:utf-8
# author:杨淑娟

from demo1 import *   # 这种导入方法，无法导 函数名前有下划线的函数
print(external_func())
#print(_internal_func())  # NameError: name '_internal_func' is not defined

# 而以下的这种方式则可以
import demo1
print(demo1._internal_func())