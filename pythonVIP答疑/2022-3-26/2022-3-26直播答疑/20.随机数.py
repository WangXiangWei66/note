# coding:utf-8
# author:杨淑娟
import random

def fun(m,n):  # 定义一个函数 ，m表示行，n表示列
    total=[]    # 用于存储每行的数据 ，每行是一个列表
    for i in range(1,m+1):   # 外层循环，  行
        lst=[]           # 用于存储每列的数据
        for j in range(1,n+1):  #内层循环，   列
            lst.append(random.randint(1,100))  # 向存储列元素的列表中添加随机数 [1,100]
        total.append(lst)  # 将该列元素添加到行中
    return total  # 返回所以数据

result=fun(5,4)  # 调用函数 ,产生一个5行，4列的数据
for row in result: # 遍历行
    for colum in row : # 从行中遍历列
        print(colum,end='\t')
    print() # 换行

