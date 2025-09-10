# coding:utf-8
# author:杨淑娟
import matplotlib.pyplot as plt
import random
plt.figure(figsize=(5,3),dpi=100)
figure,axes=plt.subplots(2,2) # 两行两列

# 在第一个绘图区域绘制折线图
axes[0,0].plot([1,2,3,4,5],[random.randint(1,10)for i in range(5)])

# 第二个绘图区域绘制散点图
axes[0,1].plot([1,2,3,4,5],[random.randint(1,10)for i in range(5)],'ro')

# 第三个绘图区域绘制柱状图
x=[1,2,3,4,5]
y=[random.randint(10,50)for i in range(5)]

axes[1,0].bar(x,y)

# 第四个绘图区域绘制饼图
x=[random.randint(10,50)for i in range(5)]

axes[1,1].pie(x,autopct='%1.1f%%')
plt.savefig('b.jpg')
plt.show()