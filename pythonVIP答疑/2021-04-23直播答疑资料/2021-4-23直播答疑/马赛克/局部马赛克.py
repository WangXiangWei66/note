# 教育机构：马士兵教育
# 讲    师：杨淑娟

import numpy as np
import pylab
import matplotlib.pyplot as plt
panda = plt.imread('24.jpg')
head=panda[100:270,100:300] # 截出头部像素点
print(head.shape)
#[a,b] a代表垂直方向坐标，b代表水平方向坐标
head2=head[::10,::10]
plt.imshow(head2);
print(head2.shape)
newpanda=panda.copy()
for i in range(17):
    for j in range(20):
        newpanda[100+i*10:110+i*10,100+j*10:110+j*10]=head2[i][j]
plt.imshow(newpanda)
pylab.show()