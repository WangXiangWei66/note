# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import numpy as np
n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
#求和
print(n.sum()) # 整个数组求
print(n.sum(axis=0)) # 表示行求和 1+4+7
print(n.sum(axis=1))  #表示列求和 1+2+3
