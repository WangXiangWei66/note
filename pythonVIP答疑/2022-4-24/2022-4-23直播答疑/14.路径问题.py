# coding:utf-8
# author:杨淑娟
import os
print(os.getcwd()) # 获取当前路径


# 第一种方式
file=open('a.txt','w')

# 第二种方式
file=open(os.getcwd()+'/a.txt','w')