# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import my
print(my.calc(10,20))  # 在调用函数时，需要把模块名称写上

from my import calc   #在调用函数时，不需要加模块名，直接写函数名即可
print(calc(10,20))

