#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import random
d={
    's01':['马丁','意大利',3.1,7,21.7],
    's02':['拖马斯','西班牙',89,34,97]
}


for item in d:  # 遍历出的结为key
    d[item].append(random.randint(1,100))
print(d)