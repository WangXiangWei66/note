# 教育机构：马士兵教育
# 讲    师：杨淑娟
# # 如何导入module_A中的数据
#（1）使用from 包名 import 模块名
# from packagetest import module_A
# print(module_A.a)

#(2) import 包名.模块名.变量名
# import packagetest.module_A
# print(packagetest.module_A.a)

#（3）import 包名
# 导入包时，本质上是将包下的__init__.py执行一遍

import  packagetest
print(packagetest.b) # 20
print(packagetest.module_A.a) # 10
