#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
a=range(1,11) # 省略了step，默认为1
print(a,type(a))
for i in a:
    print(i)

b=range(1,11,3) # 步长为3
print(list(b))

# 步长可正可负
c=range(0,-10,-2) # 步长为负数
print(list(c))

# random是随机数，每次只产生一个，如果需要多个则需要循环
import random
print(random.randint(1,10)) # 产生一个1-10之间的整数 [1,10]



