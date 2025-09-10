# coding:utf-8
# author:杨淑娟
import  numpy as np
l=np.array([[[1,2,3],[4,5,6]],[[1,4,7],[3,6,9]]])
print(l)
print("*"*10)

l[:,:,1]=np.ones((2,1))  # np.ones(2,2)形状是一个两行两列，元素都是1 ， np.ones(2,1)不报错，numpy中有个叫广播机制
print(l[:,:,1])
