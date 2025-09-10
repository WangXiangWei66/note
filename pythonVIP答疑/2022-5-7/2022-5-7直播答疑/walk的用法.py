# coding:utf-8
# author:杨淑娟
import os
path =os.getcwd() # 获取当前文件的path
print(path)
# 相当于递归操作，遍历当前路径下的所有文件，及子文件
for root,dirs,files in os.walk(path):
        print(root,dirs,files)
