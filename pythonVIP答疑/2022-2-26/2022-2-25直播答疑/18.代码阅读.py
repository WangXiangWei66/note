# coding:utf-8
# author:杨淑娟'
import numpy as np
def read_data(path):
    with open(path) as f:  # 文件读取，读取文件中的内容
        lines=f.readlines()    # 读取文件中所有内容， 结果是列表
    lines=[eval(line) for line in lines]   # 从列表中遍历第一行
    print(lines)

    #print(lines)

    x,y=zip(*lines)  # *lines相当于 是三个元组， 对三个元组对应位置 上的元素进行打包

    x=np.array(x)
    y=np.array(y)
    return x,y

x_tarin,y_train=read_data('data.csv')   # csv类型的文件，叫逗号分隔值
print(x_tarin,y_train)

# lst=[10,20,30]
# lst2=['a','b','c','d']
# zip=zip(lst,lst2)  # 对应位置 元素进行打包
# for item in zip:
#     print(item)